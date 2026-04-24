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
    from datadog_api_client.v2.model.synthetics_test_result_file_ref import SyntheticsTestResultFileRef


class SyntheticsTestResultRequestInfo(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_file_ref import SyntheticsTestResultFileRef

        return {
            "allow_insecure": (bool,),
            "body": (str,),
            "call_type": (str,),
            "destination_service": (str,),
            "dns_server": (str,),
            "dns_server_port": (int,),
            "e2e_queries": (int,),
            "files": ([SyntheticsTestResultFileRef],),
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
            "host": (str,),
            "max_ttl": (int,),
            "message": (str,),
            "method": (str,),
            "no_saving_response_body": (bool,),
            "port": (
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
            ),
            "service": (str,),
            "source_service": (str,),
            "timeout": (int,),
            "tool_name": (str,),
            "traceroute_queries": (int,),
            "url": (str,),
        }

    attribute_map = {
        "allow_insecure": "allow_insecure",
        "body": "body",
        "call_type": "call_type",
        "destination_service": "destination_service",
        "dns_server": "dns_server",
        "dns_server_port": "dns_server_port",
        "e2e_queries": "e2e_queries",
        "files": "files",
        "headers": "headers",
        "host": "host",
        "max_ttl": "max_ttl",
        "message": "message",
        "method": "method",
        "no_saving_response_body": "no_saving_response_body",
        "port": "port",
        "service": "service",
        "source_service": "source_service",
        "timeout": "timeout",
        "tool_name": "tool_name",
        "traceroute_queries": "traceroute_queries",
        "url": "url",
    }

    def __init__(
        self_,
        allow_insecure: Union[bool, UnsetType] = unset,
        body: Union[str, UnsetType] = unset,
        call_type: Union[str, UnsetType] = unset,
        destination_service: Union[str, UnsetType] = unset,
        dns_server: Union[str, UnsetType] = unset,
        dns_server_port: Union[int, UnsetType] = unset,
        e2e_queries: Union[int, UnsetType] = unset,
        files: Union[List[SyntheticsTestResultFileRef], UnsetType] = unset,
        headers: Union[Dict[str, Any], UnsetType] = unset,
        host: Union[str, UnsetType] = unset,
        max_ttl: Union[int, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        method: Union[str, UnsetType] = unset,
        no_saving_response_body: Union[bool, UnsetType] = unset,
        port: Union[Any, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        source_service: Union[str, UnsetType] = unset,
        timeout: Union[int, UnsetType] = unset,
        tool_name: Union[str, UnsetType] = unset,
        traceroute_queries: Union[int, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the outgoing request made during the test execution.

        :param allow_insecure: Whether insecure certificates are allowed for this request.
        :type allow_insecure: bool, optional

        :param body: Body sent with the request.
        :type body: str, optional

        :param call_type: gRPC call type (for example, ``unary`` , ``healthCheck`` , or ``reflection`` ).
        :type call_type: str, optional

        :param destination_service: Destination service for a Network Path test.
        :type destination_service: str, optional

        :param dns_server: DNS server used to resolve the target host.
        :type dns_server: str, optional

        :param dns_server_port: Port of the DNS server used for resolution.
        :type dns_server_port: int, optional

        :param e2e_queries: Number of end-to-end probe queries issued.
        :type e2e_queries: int, optional

        :param files: Files attached to the request.
        :type files: [SyntheticsTestResultFileRef], optional

        :param headers: Headers sent with the request.
        :type headers: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param host: Host targeted by the request.
        :type host: str, optional

        :param max_ttl: Maximum TTL for network probe packets.
        :type max_ttl: int, optional

        :param message: Message sent with the request (for WebSocket/TCP/UDP tests).
        :type message: str, optional

        :param method: HTTP method used for the request.
        :type method: str, optional

        :param no_saving_response_body: Whether the response body was not saved.
        :type no_saving_response_body: bool, optional

        :param port: Port targeted by the request. Can be a number or a string variable reference.
        :type port: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param service: Service name targeted by the request (for gRPC tests).
        :type service: str, optional

        :param source_service: Source service for a Network Path test.
        :type source_service: str, optional

        :param timeout: Request timeout in milliseconds.
        :type timeout: int, optional

        :param tool_name: Name of the MCP tool called (MCP tests only).
        :type tool_name: str, optional

        :param traceroute_queries: Number of traceroute probe queries issued.
        :type traceroute_queries: int, optional

        :param url: URL targeted by the request.
        :type url: str, optional
        """
        if allow_insecure is not unset:
            kwargs["allow_insecure"] = allow_insecure
        if body is not unset:
            kwargs["body"] = body
        if call_type is not unset:
            kwargs["call_type"] = call_type
        if destination_service is not unset:
            kwargs["destination_service"] = destination_service
        if dns_server is not unset:
            kwargs["dns_server"] = dns_server
        if dns_server_port is not unset:
            kwargs["dns_server_port"] = dns_server_port
        if e2e_queries is not unset:
            kwargs["e2e_queries"] = e2e_queries
        if files is not unset:
            kwargs["files"] = files
        if headers is not unset:
            kwargs["headers"] = headers
        if host is not unset:
            kwargs["host"] = host
        if max_ttl is not unset:
            kwargs["max_ttl"] = max_ttl
        if message is not unset:
            kwargs["message"] = message
        if method is not unset:
            kwargs["method"] = method
        if no_saving_response_body is not unset:
            kwargs["no_saving_response_body"] = no_saving_response_body
        if port is not unset:
            kwargs["port"] = port
        if service is not unset:
            kwargs["service"] = service
        if source_service is not unset:
            kwargs["source_service"] = source_service
        if timeout is not unset:
            kwargs["timeout"] = timeout
        if tool_name is not unset:
            kwargs["tool_name"] = tool_name
        if traceroute_queries is not unset:
            kwargs["traceroute_queries"] = traceroute_queries
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
