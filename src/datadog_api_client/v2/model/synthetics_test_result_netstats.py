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
    from datadog_api_client.v2.model.synthetics_test_result_netstats_hops import SyntheticsTestResultNetstatsHops
    from datadog_api_client.v2.model.synthetics_test_result_network_latency import SyntheticsTestResultNetworkLatency


class SyntheticsTestResultNetstats(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_netstats_hops import SyntheticsTestResultNetstatsHops
        from datadog_api_client.v2.model.synthetics_test_result_network_latency import (
            SyntheticsTestResultNetworkLatency,
        )

        return {
            "hops": (SyntheticsTestResultNetstatsHops,),
            "jitter": (float,),
            "latency": (SyntheticsTestResultNetworkLatency,),
            "packet_loss_percentage": (float,),
            "packets_received": (int,),
            "packets_sent": (int,),
        }

    attribute_map = {
        "hops": "hops",
        "jitter": "jitter",
        "latency": "latency",
        "packet_loss_percentage": "packet_loss_percentage",
        "packets_received": "packets_received",
        "packets_sent": "packets_sent",
    }

    def __init__(
        self_,
        hops: Union[SyntheticsTestResultNetstatsHops, UnsetType] = unset,
        jitter: Union[float, UnsetType] = unset,
        latency: Union[SyntheticsTestResultNetworkLatency, UnsetType] = unset,
        packet_loss_percentage: Union[float, UnsetType] = unset,
        packets_received: Union[int, UnsetType] = unset,
        packets_sent: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Aggregated network statistics from the test execution.

        :param hops: Statistics about the number of hops for a network test.
        :type hops: SyntheticsTestResultNetstatsHops, optional

        :param jitter: Network jitter in milliseconds.
        :type jitter: float, optional

        :param latency: Latency statistics for a network probe.
        :type latency: SyntheticsTestResultNetworkLatency, optional

        :param packet_loss_percentage: Percentage of probe packets lost.
        :type packet_loss_percentage: float, optional

        :param packets_received: Number of probe packets received.
        :type packets_received: int, optional

        :param packets_sent: Number of probe packets sent.
        :type packets_sent: int, optional
        """
        if hops is not unset:
            kwargs["hops"] = hops
        if jitter is not unset:
            kwargs["jitter"] = jitter
        if latency is not unset:
            kwargs["latency"] = latency
        if packet_loss_percentage is not unset:
            kwargs["packet_loss_percentage"] = packet_loss_percentage
        if packets_received is not unset:
            kwargs["packets_received"] = packets_received
        if packets_sent is not unset:
            kwargs["packets_sent"] = packets_sent
        super().__init__(kwargs)
