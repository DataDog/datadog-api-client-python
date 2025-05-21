# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsAPITestStepSubtype(ModelSimple):
    """
    The subtype of the Synthetic multi-step API test step.

    :param value: Must be one of ["http", "grpc", "ssl", "dns", "tcp", "udp", "icmp", "websocket"].
    :type value: str
    """

    allowed_values = {
        "http",
        "grpc",
        "ssl",
        "dns",
        "tcp",
        "udp",
        "icmp",
        "websocket",
    }
    HTTP: ClassVar["SyntheticsAPITestStepSubtype"]
    GRPC: ClassVar["SyntheticsAPITestStepSubtype"]
    SSL: ClassVar["SyntheticsAPITestStepSubtype"]
    DNS: ClassVar["SyntheticsAPITestStepSubtype"]
    TCP: ClassVar["SyntheticsAPITestStepSubtype"]
    UDP: ClassVar["SyntheticsAPITestStepSubtype"]
    ICMP: ClassVar["SyntheticsAPITestStepSubtype"]
    WEBSOCKET: ClassVar["SyntheticsAPITestStepSubtype"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsAPITestStepSubtype.HTTP = SyntheticsAPITestStepSubtype("http")
SyntheticsAPITestStepSubtype.GRPC = SyntheticsAPITestStepSubtype("grpc")
SyntheticsAPITestStepSubtype.SSL = SyntheticsAPITestStepSubtype("ssl")
SyntheticsAPITestStepSubtype.DNS = SyntheticsAPITestStepSubtype("dns")
SyntheticsAPITestStepSubtype.TCP = SyntheticsAPITestStepSubtype("tcp")
SyntheticsAPITestStepSubtype.UDP = SyntheticsAPITestStepSubtype("udp")
SyntheticsAPITestStepSubtype.ICMP = SyntheticsAPITestStepSubtype("icmp")
SyntheticsAPITestStepSubtype.WEBSOCKET = SyntheticsAPITestStepSubtype("websocket")
