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
            "tcp_delivered_ce": (int,),
            "tcp_established_connections": (int,),
            "tcp_probe0_count": (int,),
            "tcp_rcv_ooo_pack": (int,),
            "tcp_recovery_count": (int,),
            "tcp_refusals": (int,),
            "tcp_reord_seen": (int,),
            "tcp_resets": (int,),
            "tcp_retransmits": (int,),
            "tcp_rto_count": (int,),
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
        "tcp_delivered_ce": "tcp_delivered_ce",
        "tcp_established_connections": "tcp_established_connections",
        "tcp_probe0_count": "tcp_probe0_count",
        "tcp_rcv_ooo_pack": "tcp_rcv_ooo_pack",
        "tcp_recovery_count": "tcp_recovery_count",
        "tcp_refusals": "tcp_refusals",
        "tcp_reord_seen": "tcp_reord_seen",
        "tcp_resets": "tcp_resets",
        "tcp_retransmits": "tcp_retransmits",
        "tcp_rto_count": "tcp_rto_count",
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
        tcp_delivered_ce: Union[int, UnsetType] = unset,
        tcp_established_connections: Union[int, UnsetType] = unset,
        tcp_probe0_count: Union[int, UnsetType] = unset,
        tcp_rcv_ooo_pack: Union[int, UnsetType] = unset,
        tcp_recovery_count: Union[int, UnsetType] = unset,
        tcp_refusals: Union[int, UnsetType] = unset,
        tcp_reord_seen: Union[int, UnsetType] = unset,
        tcp_resets: Union[int, UnsetType] = unset,
        tcp_retransmits: Union[int, UnsetType] = unset,
        tcp_rto_count: Union[int, UnsetType] = unset,
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

        :param tcp_delivered_ce: The number of TCP segments acknowledged with the ECN Congestion Experienced (CE) mark, indicating that an upstream router marked packets as experiencing congestion.
        :type tcp_delivered_ce: int, optional

        :param tcp_established_connections: The number of TCP connections in an established state. Measured in connections per second from the client.
        :type tcp_established_connections: int, optional

        :param tcp_probe0_count: The number of TCP zero-window probes sent. These probes are sent when the receiver advertises a zero receive window, indicating it cannot accept more data.
        :type tcp_probe0_count: int, optional

        :param tcp_rcv_ooo_pack: The number of TCP packets received out of order. This indicates network-level packet reordering, which can degrade TCP performance by triggering spurious retransmissions and reducing throughput.
        :type tcp_rcv_ooo_pack: int, optional

        :param tcp_recovery_count: The number of TCP fast recovery events. Fast recovery retransmits lost segments detected through duplicate ACKs or selective acknowledgment (SACK) without waiting for a retransmission timeout.
        :type tcp_recovery_count: int, optional

        :param tcp_refusals: The number of TCP connections that were refused by the server. Typically this indicates an attempt to connect to an IP/port that is not receiving connections, or a firewall/security misconfiguration.
        :type tcp_refusals: int, optional

        :param tcp_reord_seen: The number of times reordering of sent packets was detected. Reordering detection adjusts the duplicate ACK threshold, preventing spurious retransmissions caused by out-of-order delivery.
        :type tcp_reord_seen: int, optional

        :param tcp_resets: The number of TCP connections that were reset by the server.
        :type tcp_resets: int, optional

        :param tcp_retransmits: TCP Retransmits represent detected failures that are retransmitted to ensure delivery. Measured in count of retransmits from the client.
        :type tcp_retransmits: int, optional

        :param tcp_rto_count: The number of TCP retransmission timeouts (RTOs). An RTO occurs when an ACK is not received within the estimated round-trip time, forcing the sender to retransmit and halve its congestion window.
        :type tcp_rto_count: int, optional

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
        if tcp_delivered_ce is not unset:
            kwargs["tcp_delivered_ce"] = tcp_delivered_ce
        if tcp_established_connections is not unset:
            kwargs["tcp_established_connections"] = tcp_established_connections
        if tcp_probe0_count is not unset:
            kwargs["tcp_probe0_count"] = tcp_probe0_count
        if tcp_rcv_ooo_pack is not unset:
            kwargs["tcp_rcv_ooo_pack"] = tcp_rcv_ooo_pack
        if tcp_recovery_count is not unset:
            kwargs["tcp_recovery_count"] = tcp_recovery_count
        if tcp_refusals is not unset:
            kwargs["tcp_refusals"] = tcp_refusals
        if tcp_reord_seen is not unset:
            kwargs["tcp_reord_seen"] = tcp_reord_seen
        if tcp_resets is not unset:
            kwargs["tcp_resets"] = tcp_resets
        if tcp_retransmits is not unset:
            kwargs["tcp_retransmits"] = tcp_retransmits
        if tcp_rto_count is not unset:
            kwargs["tcp_rto_count"] = tcp_rto_count
        if tcp_timeouts is not unset:
            kwargs["tcp_timeouts"] = tcp_timeouts
        super().__init__(kwargs)
