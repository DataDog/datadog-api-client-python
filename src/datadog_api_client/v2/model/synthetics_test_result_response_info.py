# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_cdn_provider_info import SyntheticsTestResultCdnProviderInfo
    from datadog_api_client.v2.model.synthetics_test_result_web_socket_close import SyntheticsTestResultWebSocketClose
    from datadog_api_client.v2.model.synthetics_test_result_health_check import SyntheticsTestResultHealthCheck
    from datadog_api_client.v2.model.synthetics_test_result_dns_record import SyntheticsTestResultDnsRecord
    from datadog_api_client.v2.model.synthetics_test_result_redirect import SyntheticsTestResultRedirect


class SyntheticsTestResultResponseInfo(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_cdn_provider_info import (
            SyntheticsTestResultCdnProviderInfo,
        )
        from datadog_api_client.v2.model.synthetics_test_result_web_socket_close import (
            SyntheticsTestResultWebSocketClose,
        )
        from datadog_api_client.v2.model.synthetics_test_result_health_check import SyntheticsTestResultHealthCheck
        from datadog_api_client.v2.model.synthetics_test_result_dns_record import SyntheticsTestResultDnsRecord
        from datadog_api_client.v2.model.synthetics_test_result_redirect import SyntheticsTestResultRedirect

        return {
            "body": (str,),
            "body_compressed": (str,),
            "body_hashes": (str,),
            "body_size": (int,),
            "cache_headers": ({str: (str,)},),
            "cdn": (SyntheticsTestResultCdnProviderInfo,),
            "close": (SyntheticsTestResultWebSocketClose,),
            "compressed_message": (str,),
            "headers": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "healthcheck": (SyntheticsTestResultHealthCheck,),
            "http_version": (str,),
            "is_body_truncated": (bool,),
            "is_message_truncated": (bool,),
            "message": (str,),
            "metadata": ({str: (str,)},),
            "records": ([SyntheticsTestResultDnsRecord],),
            "redirects": ([SyntheticsTestResultRedirect],),
            "status_code": (int,),
        }

    attribute_map = {
        "body": "body",
        "body_compressed": "body_compressed",
        "body_hashes": "body_hashes",
        "body_size": "body_size",
        "cache_headers": "cache_headers",
        "cdn": "cdn",
        "close": "close",
        "compressed_message": "compressed_message",
        "headers": "headers",
        "healthcheck": "healthcheck",
        "http_version": "http_version",
        "is_body_truncated": "is_body_truncated",
        "is_message_truncated": "is_message_truncated",
        "message": "message",
        "metadata": "metadata",
        "records": "records",
        "redirects": "redirects",
        "status_code": "status_code",
    }

    def __init__(
        self_,
        body: Union[str, UnsetType] = unset,
        body_compressed: Union[str, UnsetType] = unset,
        body_hashes: Union[str, UnsetType] = unset,
        body_size: Union[int, UnsetType] = unset,
        cache_headers: Union[Dict[str, str], UnsetType] = unset,
        cdn: Union[SyntheticsTestResultCdnProviderInfo, UnsetType] = unset,
        close: Union[SyntheticsTestResultWebSocketClose, UnsetType] = unset,
        compressed_message: Union[str, UnsetType] = unset,
        headers: Union[Dict[str, Any], UnsetType] = unset,
        healthcheck: Union[SyntheticsTestResultHealthCheck, UnsetType] = unset,
        http_version: Union[str, UnsetType] = unset,
        is_body_truncated: Union[bool, UnsetType] = unset,
        is_message_truncated: Union[bool, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        metadata: Union[Dict[str, str], UnsetType] = unset,
        records: Union[List[SyntheticsTestResultDnsRecord], UnsetType] = unset,
        redirects: Union[List[SyntheticsTestResultRedirect], UnsetType] = unset,
        status_code: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the response received during the test execution.

        :param body: Body of the response.
        :type body: str, optional

        :param body_compressed: Compressed representation of the response body.
        :type body_compressed: str, optional

        :param body_hashes: Hashes computed over the response body.
        :type body_hashes: str, optional

        :param body_size: Size of the response body in bytes.
        :type body_size: int, optional

        :param cache_headers: Cache-related response headers.
        :type cache_headers: {str: (str,)}, optional

        :param cdn: CDN provider details inferred from response headers.
        :type cdn: SyntheticsTestResultCdnProviderInfo, optional

        :param close: WebSocket close frame information for WebSocket test responses.
        :type close: SyntheticsTestResultWebSocketClose, optional

        :param compressed_message: Compressed representation of the response message.
        :type compressed_message: str, optional

        :param headers: Response headers.
        :type headers: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param healthcheck: Health check information returned from a gRPC health check call.
        :type healthcheck: SyntheticsTestResultHealthCheck, optional

        :param http_version: HTTP version of the response.
        :type http_version: str, optional

        :param is_body_truncated: Whether the response body was truncated.
        :type is_body_truncated: bool, optional

        :param is_message_truncated: Whether the response message was truncated.
        :type is_message_truncated: bool, optional

        :param message: Message received in the response (for WebSocket/TCP/UDP tests).
        :type message: str, optional

        :param metadata: Additional metadata returned with the response.
        :type metadata: {str: (str,)}, optional

        :param records: DNS records returned in the response (DNS tests only).
        :type records: [SyntheticsTestResultDnsRecord], optional

        :param redirects: Redirect hops encountered while performing the request.
        :type redirects: [SyntheticsTestResultRedirect], optional

        :param status_code: HTTP status code of the response.
        :type status_code: int, optional
        """
        if body is not unset:
            kwargs["body"] = body
        if body_compressed is not unset:
            kwargs["body_compressed"] = body_compressed
        if body_hashes is not unset:
            kwargs["body_hashes"] = body_hashes
        if body_size is not unset:
            kwargs["body_size"] = body_size
        if cache_headers is not unset:
            kwargs["cache_headers"] = cache_headers
        if cdn is not unset:
            kwargs["cdn"] = cdn
        if close is not unset:
            kwargs["close"] = close
        if compressed_message is not unset:
            kwargs["compressed_message"] = compressed_message
        if headers is not unset:
            kwargs["headers"] = headers
        if healthcheck is not unset:
            kwargs["healthcheck"] = healthcheck
        if http_version is not unset:
            kwargs["http_version"] = http_version
        if is_body_truncated is not unset:
            kwargs["is_body_truncated"] = is_body_truncated
        if is_message_truncated is not unset:
            kwargs["is_message_truncated"] = is_message_truncated
        if message is not unset:
            kwargs["message"] = message
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if records is not unset:
            kwargs["records"] = records
        if redirects is not unset:
            kwargs["redirects"] = redirects
        if status_code is not unset:
            kwargs["status_code"] = status_code
        super().__init__(kwargs)
