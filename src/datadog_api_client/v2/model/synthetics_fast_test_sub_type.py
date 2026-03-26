# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsFastTestSubType(ModelSimple):
    """
    Subtype of the Synthetic test that produced this result.

    :param value: Must be one of ["dns", "grpc", "http", "icmp", "mcp", "multi", "ssl", "tcp", "udp", "websocket"].
    :type value: str
    """

    allowed_values = {
        "dns",
        "grpc",
        "http",
        "icmp",
        "mcp",
        "multi",
        "ssl",
        "tcp",
        "udp",
        "websocket",
    }
    DNS: ClassVar["SyntheticsFastTestSubType"]
    GRPC: ClassVar["SyntheticsFastTestSubType"]
    HTTP: ClassVar["SyntheticsFastTestSubType"]
    ICMP: ClassVar["SyntheticsFastTestSubType"]
    MCP: ClassVar["SyntheticsFastTestSubType"]
    MULTI: ClassVar["SyntheticsFastTestSubType"]
    SSL: ClassVar["SyntheticsFastTestSubType"]
    TCP: ClassVar["SyntheticsFastTestSubType"]
    UDP: ClassVar["SyntheticsFastTestSubType"]
    WEBSOCKET: ClassVar["SyntheticsFastTestSubType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsFastTestSubType.DNS = SyntheticsFastTestSubType("dns")
SyntheticsFastTestSubType.GRPC = SyntheticsFastTestSubType("grpc")
SyntheticsFastTestSubType.HTTP = SyntheticsFastTestSubType("http")
SyntheticsFastTestSubType.ICMP = SyntheticsFastTestSubType("icmp")
SyntheticsFastTestSubType.MCP = SyntheticsFastTestSubType("mcp")
SyntheticsFastTestSubType.MULTI = SyntheticsFastTestSubType("multi")
SyntheticsFastTestSubType.SSL = SyntheticsFastTestSubType("ssl")
SyntheticsFastTestSubType.TCP = SyntheticsFastTestSubType("tcp")
SyntheticsFastTestSubType.UDP = SyntheticsFastTestSubType("udp")
SyntheticsFastTestSubType.WEBSOCKET = SyntheticsFastTestSubType("websocket")
