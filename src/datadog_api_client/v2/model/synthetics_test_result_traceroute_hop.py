# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_network_latency import SyntheticsTestResultNetworkLatency
    from datadog_api_client.v2.model.synthetics_test_result_router import SyntheticsTestResultRouter


class SyntheticsTestResultTracerouteHop(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_network_latency import (
            SyntheticsTestResultNetworkLatency,
        )
        from datadog_api_client.v2.model.synthetics_test_result_router import SyntheticsTestResultRouter

        return {
            "host": (str,),
            "latency": (SyntheticsTestResultNetworkLatency,),
            "packet_loss_percentage": (float,),
            "packet_size": (int,),
            "packets_received": (int,),
            "packets_sent": (int,),
            "resolved_ip": (str,),
            "routers": ([SyntheticsTestResultRouter],),
        }

    attribute_map = {
        "host": "host",
        "latency": "latency",
        "packet_loss_percentage": "packet_loss_percentage",
        "packet_size": "packet_size",
        "packets_received": "packets_received",
        "packets_sent": "packets_sent",
        "resolved_ip": "resolved_ip",
        "routers": "routers",
    }

    def __init__(
        self_,
        host: Union[str, UnsetType] = unset,
        latency: Union[SyntheticsTestResultNetworkLatency, UnsetType] = unset,
        packet_loss_percentage: Union[float, UnsetType] = unset,
        packet_size: Union[int, UnsetType] = unset,
        packets_received: Union[int, UnsetType] = unset,
        packets_sent: Union[int, UnsetType] = unset,
        resolved_ip: Union[str, UnsetType] = unset,
        routers: Union[List[SyntheticsTestResultRouter], UnsetType] = unset,
        **kwargs,
    ):
        """
        A network probe result, used for traceroute hops and ping summaries.

        :param host: Target hostname.
        :type host: str, optional

        :param latency: Latency statistics for a network probe.
        :type latency: SyntheticsTestResultNetworkLatency, optional

        :param packet_loss_percentage: Percentage of probe packets lost.
        :type packet_loss_percentage: float, optional

        :param packet_size: Size of each probe packet in bytes.
        :type packet_size: int, optional

        :param packets_received: Number of probe packets received.
        :type packets_received: int, optional

        :param packets_sent: Number of probe packets sent.
        :type packets_sent: int, optional

        :param resolved_ip: Resolved IP address for the target.
        :type resolved_ip: str, optional

        :param routers: List of intermediate routers for the traceroute.
        :type routers: [SyntheticsTestResultRouter], optional
        """
        if host is not unset:
            kwargs["host"] = host
        if latency is not unset:
            kwargs["latency"] = latency
        if packet_loss_percentage is not unset:
            kwargs["packet_loss_percentage"] = packet_loss_percentage
        if packet_size is not unset:
            kwargs["packet_size"] = packet_size
        if packets_received is not unset:
            kwargs["packets_received"] = packets_received
        if packets_sent is not unset:
            kwargs["packets_sent"] = packets_sent
        if resolved_ip is not unset:
            kwargs["resolved_ip"] = resolved_ip
        if routers is not unset:
            kwargs["routers"] = routers
        super().__init__(kwargs)
