# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.

import json
import logging
import re
import ssl
from urllib.parse import urlencode
import zlib
import urllib3  # type: ignore

from datadog_api_client.exceptions import (
    ApiException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException,
    ServiceException,
    ApiValueError,
)


logger = logging.getLogger(__name__)


RETRY_AFTER_STATUS_CODES = frozenset([429, 500, 501, 502, 503, 504, 505, 506, 507, 509, 510, 511])
RETRY_ALLOWED_METHODS = frozenset(["GET", "PUT", "DELETE", "POST", "PATCH"])


class ClientRetry(urllib3.util.Retry):
    RETRY_AFTER_STATUS_CODES = RETRY_AFTER_STATUS_CODES
    DEFAULT_ALLOWED_METHODS = RETRY_ALLOWED_METHODS

    def get_retry_after(self, response):
        """
        This method overrides the default "Retry-after" header and uses dd's X-Ratelimit-Reset header
        and gets the value of X-Ratelimit-Reset in seconds.
        """
        retry_after = response.headers.get("X-Ratelimit-Reset")

        if retry_after is None:
            return None
        return self.parse_retry_after(retry_after)

    def is_retry(self, method, status_code, has_retry_after=False):
        if method not in self.DEFAULT_ALLOWED_METHODS:
            return False

        if self.status_forcelist and status_code in self.status_forcelist:
            return True
        return self.total and self.respect_retry_after_header and (status_code in self.RETRY_AFTER_STATUS_CODES)


class RESTClientObject:
    def __init__(self, configuration, pools_size=4, maxsize=4):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680
        # maxsize is the number of requests to host that are allowed in parallel
        # Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html

        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        addition_pool_args = {}
        if configuration.assert_hostname is not None:
            addition_pool_args["assert_hostname"] = configuration.assert_hostname

        if configuration.enable_retry:
            retries = ClientRetry(
                total=configuration.max_retries,
                backoff_factor=configuration.retry_backoff_factor,
            )
            addition_pool_args["retries"] = retries

        if configuration.socket_options is not None:
            addition_pool_args["socket_options"] = configuration.socket_options

        # https pool manager
        if configuration.proxy:
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=configuration.ssl_ca_cert,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                proxy_headers=configuration.proxy_headers,
                **addition_pool_args,
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=configuration.ssl_ca_cert,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                **addition_pool_args,
            )

    def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        body=None,
        post_params=None,
        preload_content=True,
        request_timeout=None,
    ):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
        :param request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
        """
        method = method.upper()

        if post_params and body:
            raise ApiValueError("body parameter cannot be used with post_params parameter.")

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if request_timeout:
            if isinstance(request_timeout, (int, float)):
                timeout = urllib3.Timeout(total=request_timeout)
            elif isinstance(request_timeout, tuple) and len(request_timeout) == 2:
                timeout = urllib3.Timeout(connect=request_timeout[0], read=request_timeout[1])

        try:
            request_kwargs = {}
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ("POST", "PUT", "PATCH", "OPTIONS", "DELETE"):
                # Only set a default Content-Type for POST, PUT, PATCH and OPTIONS requests
                if method != "DELETE" and "Content-Type" not in headers:
                    headers["Content-Type"] = "application/json"
                if query_params:
                    url += "?" + urlencode(query_params)
                if "Content-Type" not in headers or re.search("json", headers["Content-Type"], re.IGNORECASE):
                    request_body = None
                    if body is not None:
                        request_body = json.dumps(body)
                        if headers.get("Content-Encoding") == "gzip":
                            compressor = zlib.compressobj(wbits=16 + zlib.MAX_WBITS)
                            request_body = compressor.compress(request_body.encode("utf-8")) + compressor.flush()
                        elif headers.get("Content-Encoding") == "deflate":
                            request_body = zlib.compress(request_body.encode("utf-8"))
                        elif headers.get("Content-Encoding") == "zstd1":
                            import zstandard as zstd

                            compressor = zstd.ZstdCompressor()
                            request_body = compressor.compress(request_body.encode("utf-8"))
                        request_kwargs["body"] = request_body
                elif headers["Content-Type"] == "application/x-www-form-urlencoded":
                    request_kwargs["encode_multipart"] = False
                    request_kwargs["fields"] = post_params
                elif headers["Content-Type"] == "multipart/form-data":
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers["Content-Type"]
                    request_kwargs["encode_multipart"] = True
                    request_kwargs["fields"] = post_params
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, (str, bytes)):
                    request_kwargs["body"] = body
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                request_kwargs["fields"] = query_params
            r = self.pool_manager.request(
                method, url, preload_content=preload_content, timeout=timeout, headers=headers, **request_kwargs
            )
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if preload_content:
            # log response body
            logger.debug("response body: %s", r.data)

        if not 200 <= r.status <= 299:
            if r.status == 401:
                raise UnauthorizedException(http_resp=r)

            if r.status == 403:
                raise ForbiddenException(http_resp=r)

            if r.status == 404:
                raise NotFoundException(http_resp=r)

            if 500 <= r.status <= 599:
                raise ServiceException(http_resp=r)

            raise ApiException(http_resp=r)

        return r


class _AioSonicResponseWrapper:
    def __init__(self, response, data):
        self.response = response
        self.status = response.status_code
        self.reason = response.response_initial.get("reason")
        self.data = data
        self.headers = response.headers.copy()


class AsyncRESTClientObject:
    def __init__(self, configuration):
        import aiosonic  # type: ignore

        proxy = None
        if configuration.proxy:
            proxy = aiosonic.Proxy(configuration.proxy, configuration.proxy_headers)
        self._client = aiosonic.HTTPClient(proxy=proxy, verify_ssl=configuration.verify_ssl)
        self._configuration = configuration

    def _retry(self, method, response, counter):
        if (
            not self._configuration.enable_retry
            or counter >= self._configuration.max_retries
            or method not in RETRY_ALLOWED_METHODS
            or response.status_code not in RETRY_AFTER_STATUS_CODES
        ):
            return 0
        retry_after = response.headers.get("X-Ratelimit-Reset")
        if retry_after is None:
            return self._configuration.retry_backoff_factor * (2 ** (counter))
        return int(retry_after)

    async def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        body=None,
        post_params=None,
        preload_content=True,
        request_timeout=None,
    ):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param preload_content: if False, the raw HTTP response object will
                                be returned without reading/decoding response
                                data. Default is True.
        :param request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
        """
        assert not post_params, "not supported for now"
        if request_timeout is not None:
            from aiosonic.timeout import Timeouts  # type: ignore

            if isinstance(request_timeout, (int, float)):
                request_timeout = Timeouts(request_timeout=request_timeout)
            else:
                request_timeout = Timeouts(sock_connect=request_timeout[0], sock_read=request_timeout[1])
        request_body = None
        if (
            "Content-Type" not in headers
            or re.search("json", headers["Content-Type"], re.IGNORECASE)
            and body is not None
        ):
            request_body = json.dumps(body)
            if headers.get("Content-Encoding") == "gzip":
                compress = zlib.compressobj(wbits=16 + zlib.MAX_WBITS)
                request_body = compress.compress(request_body.encode("utf-8")) + compress.flush()
            elif headers.get("Content-Encoding") == "deflate":
                request_body = zlib.compress(request_body.encode("utf-8"))
            elif headers.get("Content-Encoding") == "zstd1":
                import zstandard as zstd

                compressor = zstd.ZstdCompressor()
                request_body = compressor.compress(request_body.encode("utf-8"))
        counter = 0
        while True:
            response = await self._client.request(
                url, method, headers, query_params, request_body, timeouts=request_timeout
            )
            retry = self._retry(method, response, counter)
            if not retry:
                break
            import asyncio

            await asyncio.sleep(retry)
            counter += 1

        if not 200 <= response.status_code <= 299:
            data = b""
            if preload_content:
                data = await response.content()
            r = _AioSonicResponseWrapper(response, data)

            if response.status_code == 401:
                raise UnauthorizedException(http_resp=r)

            if response.status_code == 403:
                raise ForbiddenException(http_resp=r)

            if response.status_code == 404:
                raise NotFoundException(http_resp=r)

            if 500 <= response.status_code <= 599:
                raise ServiceException(http_resp=r)

            raise ApiException(http_resp=r)

        return response
