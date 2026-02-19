# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_network_test_request_tcp_method import (
        SyntheticsNetworkTestRequestTCPMethod,
    )


class SyntheticsNetworkTestRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_network_test_request_tcp_method import (
            SyntheticsNetworkTestRequestTCPMethod,
        )

        return {
            "destination_service": (str,),
            "e2e_queries": (int,),
            "host": (str,),
            "max_ttl": (int,),
            "port": (int,),
            "source_service": (str,),
            "tcp_method": (SyntheticsNetworkTestRequestTCPMethod,),
            "timeout": (int,),
            "traceroute_queries": (int,),
        }

    attribute_map = {
        "destination_service": "destination_service",
        "e2e_queries": "e2e_queries",
        "host": "host",
        "max_ttl": "max_ttl",
        "port": "port",
        "source_service": "source_service",
        "tcp_method": "tcp_method",
        "timeout": "timeout",
        "traceroute_queries": "traceroute_queries",
    }

    def __init__(
        self_,
        e2e_queries: int,
        host: str,
        max_ttl: int,
        traceroute_queries: int,
        destination_service: Union[str, UnsetType] = unset,
        port: Union[int, UnsetType] = unset,
        source_service: Union[str, UnsetType] = unset,
        tcp_method: Union[SyntheticsNetworkTestRequestTCPMethod, UnsetType] = unset,
        timeout: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing the request for a Network Path test.

        :param destination_service: An optional label displayed for the destination host in the Network Path visualization.
        :type destination_service: str, optional

        :param e2e_queries: The number of packets sent to probe the destination to measure packet loss, latency and jitter.
        :type e2e_queries: int

        :param host: Host name to query.
        :type host: str

        :param max_ttl: The maximum time-to-live (max number of hops) used in outgoing probe packets.
        :type max_ttl: int

        :param port: For TCP or UDP tests, the port to use when performing the test.
            If not set on a UDP test, a random port is assigned, which may affect the results.
        :type port: int, optional

        :param source_service: An optional label displayed for the source host in the Network Path visualization.
        :type source_service: str, optional

        :param tcp_method: For TCP tests, the TCP traceroute strategy.
        :type tcp_method: SyntheticsNetworkTestRequestTCPMethod, optional

        :param timeout: Timeout in seconds.
        :type timeout: int, optional

        :param traceroute_queries: The number of traceroute path tracings.
        :type traceroute_queries: int
        """
        if destination_service is not unset:
            kwargs["destination_service"] = destination_service
        if port is not unset:
            kwargs["port"] = port
        if source_service is not unset:
            kwargs["source_service"] = source_service
        if tcp_method is not unset:
            kwargs["tcp_method"] = tcp_method
        if timeout is not unset:
            kwargs["timeout"] = timeout
        super().__init__(kwargs)

        self_.e2e_queries = e2e_queries
        self_.host = host
        self_.max_ttl = max_ttl
        self_.traceroute_queries = traceroute_queries
