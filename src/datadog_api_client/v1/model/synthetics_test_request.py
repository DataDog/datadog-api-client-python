# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_basic_auth import SyntheticsBasicAuth
    from datadog_api_client.v1.model.synthetics_test_request_certificate import SyntheticsTestRequestCertificate
    from datadog_api_client.v1.model.synthetics_test_headers import SyntheticsTestHeaders
    from datadog_api_client.v1.model.synthetics_test_metadata import SyntheticsTestMetadata
    from datadog_api_client.v1.model.http_method import HTTPMethod
    from datadog_api_client.v1.model.synthetics_test_request_proxy import SyntheticsTestRequestProxy
    from datadog_api_client.v1.model.synthetics_basic_auth_web import SyntheticsBasicAuthWeb
    from datadog_api_client.v1.model.synthetics_basic_auth_sigv4 import SyntheticsBasicAuthSigv4
    from datadog_api_client.v1.model.synthetics_basic_auth_ntlm import SyntheticsBasicAuthNTLM
    from datadog_api_client.v1.model.synthetics_basic_auth_digest import SyntheticsBasicAuthDigest


class SyntheticsTestRequest(ModelNormal):
    validations = {
        "dns_server_port": {
            "inclusive_maximum": 65535,
            "inclusive_minimum": 1,
        },
        "number_of_packets": {
            "inclusive_maximum": 10,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_basic_auth import SyntheticsBasicAuth
        from datadog_api_client.v1.model.synthetics_test_request_certificate import SyntheticsTestRequestCertificate
        from datadog_api_client.v1.model.synthetics_test_headers import SyntheticsTestHeaders
        from datadog_api_client.v1.model.synthetics_test_metadata import SyntheticsTestMetadata
        from datadog_api_client.v1.model.http_method import HTTPMethod
        from datadog_api_client.v1.model.synthetics_test_request_proxy import SyntheticsTestRequestProxy

        return {
            "allow_insecure": (bool,),
            "basic_auth": (SyntheticsBasicAuth,),
            "body": (str,),
            "certificate": (SyntheticsTestRequestCertificate,),
            "certificate_domains": ([str],),
            "dns_server": (str,),
            "dns_server_port": (int,),
            "follow_redirects": (bool,),
            "headers": (SyntheticsTestHeaders,),
            "host": (str,),
            "message": (str,),
            "metadata": (SyntheticsTestMetadata,),
            "method": (HTTPMethod,),
            "no_saving_response_body": (bool,),
            "number_of_packets": (int,),
            "port": (int,),
            "proxy": (SyntheticsTestRequestProxy,),
            "query": (dict,),
            "servername": (str,),
            "service": (str,),
            "should_track_hops": (bool,),
            "timeout": (float,),
            "url": (str,),
        }

    attribute_map = {
        "allow_insecure": "allow_insecure",
        "basic_auth": "basicAuth",
        "body": "body",
        "certificate": "certificate",
        "certificate_domains": "certificateDomains",
        "dns_server": "dnsServer",
        "dns_server_port": "dnsServerPort",
        "follow_redirects": "follow_redirects",
        "headers": "headers",
        "host": "host",
        "message": "message",
        "metadata": "metadata",
        "method": "method",
        "no_saving_response_body": "noSavingResponseBody",
        "number_of_packets": "numberOfPackets",
        "port": "port",
        "proxy": "proxy",
        "query": "query",
        "servername": "servername",
        "service": "service",
        "should_track_hops": "shouldTrackHops",
        "timeout": "timeout",
        "url": "url",
    }

    def __init__(
        self_,
        allow_insecure: Union[bool, UnsetType] = unset,
        basic_auth: Union[
            SyntheticsBasicAuth,
            SyntheticsBasicAuthWeb,
            SyntheticsBasicAuthSigv4,
            SyntheticsBasicAuthNTLM,
            SyntheticsBasicAuthDigest,
            UnsetType,
        ] = unset,
        body: Union[str, UnsetType] = unset,
        certificate: Union[SyntheticsTestRequestCertificate, UnsetType] = unset,
        certificate_domains: Union[List[str], UnsetType] = unset,
        dns_server: Union[str, UnsetType] = unset,
        dns_server_port: Union[int, UnsetType] = unset,
        follow_redirects: Union[bool, UnsetType] = unset,
        headers: Union[SyntheticsTestHeaders, UnsetType] = unset,
        host: Union[str, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        metadata: Union[SyntheticsTestMetadata, UnsetType] = unset,
        method: Union[HTTPMethod, UnsetType] = unset,
        no_saving_response_body: Union[bool, UnsetType] = unset,
        number_of_packets: Union[int, UnsetType] = unset,
        port: Union[int, UnsetType] = unset,
        proxy: Union[SyntheticsTestRequestProxy, UnsetType] = unset,
        query: Union[dict, UnsetType] = unset,
        servername: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        should_track_hops: Union[bool, UnsetType] = unset,
        timeout: Union[float, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing the Synthetic test request.

        :param allow_insecure: Allows loading insecure content for an HTTP request in a multistep test step.
        :type allow_insecure: bool, optional

        :param basic_auth: Object to handle basic authentication when performing the test.
        :type basic_auth: SyntheticsBasicAuth, optional

        :param body: Body to include in the test.
        :type body: str, optional

        :param certificate: Client certificate to use when performing the test request.
        :type certificate: SyntheticsTestRequestCertificate, optional

        :param certificate_domains: By default, the client certificate is applied on the domain of the starting URL for browser tests. If you want your client certificate to be applied on other domains instead, add them in ``certificateDomains``.
        :type certificate_domains: [str], optional

        :param dns_server: DNS server to use for DNS tests.
        :type dns_server: str, optional

        :param dns_server_port: DNS server port to use for DNS tests.
        :type dns_server_port: int, optional

        :param follow_redirects: Specifies whether or not the request follows redirects.
        :type follow_redirects: bool, optional

        :param headers: Headers to include when performing the test.
        :type headers: SyntheticsTestHeaders, optional

        :param host: Host name to perform the test with.
        :type host: str, optional

        :param message: Message to send for UDP or WebSocket tests.
        :type message: str, optional

        :param metadata: Metadata to include when performing the gRPC test.
        :type metadata: SyntheticsTestMetadata, optional

        :param method: The HTTP method.
        :type method: HTTPMethod, optional

        :param no_saving_response_body: Determines whether or not to save the response body.
        :type no_saving_response_body: bool, optional

        :param number_of_packets: Number of pings to use per test.
        :type number_of_packets: int, optional

        :param port: Port to use when performing the test.
        :type port: int, optional

        :param proxy: The proxy to perform the test.
        :type proxy: SyntheticsTestRequestProxy, optional

        :param query: Query to use for the test.
        :type query: dict, optional

        :param servername: For SSL tests, it specifies on which server you want to initiate the TLS handshake,
            allowing the server to present one of multiple possible certificates on
            the same IP address and TCP port number.
        :type servername: str, optional

        :param service: gRPC service on which you want to perform the healthcheck.
        :type service: str, optional

        :param should_track_hops: Turns on a traceroute probe to discover all gateways along the path to the host destination.
        :type should_track_hops: bool, optional

        :param timeout: Timeout in seconds for the test.
        :type timeout: float, optional

        :param url: URL to perform the test with.
        :type url: str, optional
        """
        if allow_insecure is not unset:
            kwargs["allow_insecure"] = allow_insecure
        if basic_auth is not unset:
            kwargs["basic_auth"] = basic_auth
        if body is not unset:
            kwargs["body"] = body
        if certificate is not unset:
            kwargs["certificate"] = certificate
        if certificate_domains is not unset:
            kwargs["certificate_domains"] = certificate_domains
        if dns_server is not unset:
            kwargs["dns_server"] = dns_server
        if dns_server_port is not unset:
            kwargs["dns_server_port"] = dns_server_port
        if follow_redirects is not unset:
            kwargs["follow_redirects"] = follow_redirects
        if headers is not unset:
            kwargs["headers"] = headers
        if host is not unset:
            kwargs["host"] = host
        if message is not unset:
            kwargs["message"] = message
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if method is not unset:
            kwargs["method"] = method
        if no_saving_response_body is not unset:
            kwargs["no_saving_response_body"] = no_saving_response_body
        if number_of_packets is not unset:
            kwargs["number_of_packets"] = number_of_packets
        if port is not unset:
            kwargs["port"] = port
        if proxy is not unset:
            kwargs["proxy"] = proxy
        if query is not unset:
            kwargs["query"] = query
        if servername is not unset:
            kwargs["servername"] = servername
        if service is not unset:
            kwargs["service"] = service
        if should_track_hops is not unset:
            kwargs["should_track_hops"] = should_track_hops
        if timeout is not unset:
            kwargs["timeout"] = timeout
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
