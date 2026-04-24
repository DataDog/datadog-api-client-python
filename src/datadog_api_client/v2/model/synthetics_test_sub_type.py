# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestSubType(ModelSimple):
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
    DNS: ClassVar["SyntheticsTestSubType"]
    GRPC: ClassVar["SyntheticsTestSubType"]
    HTTP: ClassVar["SyntheticsTestSubType"]
    ICMP: ClassVar["SyntheticsTestSubType"]
    MCP: ClassVar["SyntheticsTestSubType"]
    MULTI: ClassVar["SyntheticsTestSubType"]
    SSL: ClassVar["SyntheticsTestSubType"]
    TCP: ClassVar["SyntheticsTestSubType"]
    UDP: ClassVar["SyntheticsTestSubType"]
    WEBSOCKET: ClassVar["SyntheticsTestSubType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestSubType.DNS = SyntheticsTestSubType("dns")
SyntheticsTestSubType.GRPC = SyntheticsTestSubType("grpc")
SyntheticsTestSubType.HTTP = SyntheticsTestSubType("http")
SyntheticsTestSubType.ICMP = SyntheticsTestSubType("icmp")
SyntheticsTestSubType.MCP = SyntheticsTestSubType("mcp")
SyntheticsTestSubType.MULTI = SyntheticsTestSubType("multi")
SyntheticsTestSubType.SSL = SyntheticsTestSubType("ssl")
SyntheticsTestSubType.TCP = SyntheticsTestSubType("tcp")
SyntheticsTestSubType.UDP = SyntheticsTestSubType("udp")
SyntheticsTestSubType.WEBSOCKET = SyntheticsTestSubType("websocket")
