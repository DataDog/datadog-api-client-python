# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SingleAggregatedConnectionResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "bytes_sent_by_client": (int,),
            "bytes_sent_by_server": (int,),
            "group_bys": ({str: ([str],)},),
            "packets_sent_by_client": (int,),
            "packets_sent_by_server": (int,),
            "rtt_micro_seconds": (int,),
            "tcp_closed_connections": (int,),
            "tcp_established_connections": (int,),
            "tcp_refusals": (int,),
            "tcp_resets": (int,),
            "tcp_retransmits": (int,),
            "tcp_timeouts": (int,),
        }

    attribute_map = {
        "bytes_sent_by_client": "bytes_sent_by_client",
        "bytes_sent_by_server": "bytes_sent_by_server",
        "group_bys": "group_bys",
        "packets_sent_by_client": "packets_sent_by_client",
        "packets_sent_by_server": "packets_sent_by_server",
        "rtt_micro_seconds": "rtt_micro_seconds",
        "tcp_closed_connections": "tcp_closed_connections",
        "tcp_established_connections": "tcp_established_connections",
        "tcp_refusals": "tcp_refusals",
        "tcp_resets": "tcp_resets",
        "tcp_retransmits": "tcp_retransmits",
        "tcp_timeouts": "tcp_timeouts",
    }

    def __init__(
        self_,
        bytes_sent_by_client: Union[int, UnsetType] = unset,
        bytes_sent_by_server: Union[int, UnsetType] = unset,
        group_bys: Union[Dict[str, List[str]], UnsetType] = unset,
        packets_sent_by_client: Union[int, UnsetType] = unset,
        packets_sent_by_server: Union[int, UnsetType] = unset,
        rtt_micro_seconds: Union[int, UnsetType] = unset,
        tcp_closed_connections: Union[int, UnsetType] = unset,
        tcp_established_connections: Union[int, UnsetType] = unset,
        tcp_refusals: Union[int, UnsetType] = unset,
        tcp_resets: Union[int, UnsetType] = unset,
        tcp_retransmits: Union[int, UnsetType] = unset,
        tcp_timeouts: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for an aggregated connection.

        :param bytes_sent_by_client: The total number of bytes sent by the client over the given period.
        :type bytes_sent_by_client: int, optional

        :param bytes_sent_by_server: The total number of bytes sent by the server over the given period.
        :type bytes_sent_by_server: int, optional

        :param group_bys: The key, value pairs for each group by.
        :type group_bys: {str: ([str],)}, optional

        :param packets_sent_by_client: The total number of packets sent by the client over the given period.
        :type packets_sent_by_client: int, optional

        :param packets_sent_by_server: The total number of packets sent by the server over the given period.
        :type packets_sent_by_server: int, optional

        :param rtt_micro_seconds: Measured as TCP smoothed round trip time in microseconds (the time between a TCP frame being sent and acknowledged).
        :type rtt_micro_seconds: int, optional

        :param tcp_closed_connections: The number of TCP connections in a closed state. Measured in connections per second from the client.
        :type tcp_closed_connections: int, optional

        :param tcp_established_connections: The number of TCP connections in an established state. Measured in connections per second from the client.
        :type tcp_established_connections: int, optional

        :param tcp_refusals: The number of TCP connections that were refused by the server. Typically this indicates an attempt to connect to an IP/port that is not receiving connections, or a firewall/security misconfiguration.
        :type tcp_refusals: int, optional

        :param tcp_resets: The number of TCP connections that were reset by the server.
        :type tcp_resets: int, optional

        :param tcp_retransmits: TCP Retransmits represent detected failures that are retransmitted to ensure delivery. Measured in count of retransmits from the client.
        :type tcp_retransmits: int, optional

        :param tcp_timeouts: The number of TCP connections that timed out from the perspective of the operating system. This can indicate general connectivity and latency issues.
        :type tcp_timeouts: int, optional
        """
        if bytes_sent_by_client is not unset:
            kwargs["bytes_sent_by_client"] = bytes_sent_by_client
        if bytes_sent_by_server is not unset:
            kwargs["bytes_sent_by_server"] = bytes_sent_by_server
        if group_bys is not unset:
            kwargs["group_bys"] = group_bys
        if packets_sent_by_client is not unset:
            kwargs["packets_sent_by_client"] = packets_sent_by_client
        if packets_sent_by_server is not unset:
            kwargs["packets_sent_by_server"] = packets_sent_by_server
        if rtt_micro_seconds is not unset:
            kwargs["rtt_micro_seconds"] = rtt_micro_seconds
        if tcp_closed_connections is not unset:
            kwargs["tcp_closed_connections"] = tcp_closed_connections
        if tcp_established_connections is not unset:
            kwargs["tcp_established_connections"] = tcp_established_connections
        if tcp_refusals is not unset:
            kwargs["tcp_refusals"] = tcp_refusals
        if tcp_resets is not unset:
            kwargs["tcp_resets"] = tcp_resets
        if tcp_retransmits is not unset:
            kwargs["tcp_retransmits"] = tcp_retransmits
        if tcp_timeouts is not unset:
            kwargs["tcp_timeouts"] = tcp_timeouts
        super().__init__(kwargs)
