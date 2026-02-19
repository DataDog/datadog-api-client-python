# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsNetworkTestSubType(ModelSimple):
    """
    Subtype of the Synthetic Network Path test: `tcp`, `udp`, or `icmp`.

    :param value: Must be one of ["tcp", "udp", "icmp"].
    :type value: str
    """

    allowed_values = {
        "tcp",
        "udp",
        "icmp",
    }
    TCP: ClassVar["SyntheticsNetworkTestSubType"]
    UDP: ClassVar["SyntheticsNetworkTestSubType"]
    ICMP: ClassVar["SyntheticsNetworkTestSubType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsNetworkTestSubType.TCP = SyntheticsNetworkTestSubType("tcp")
SyntheticsNetworkTestSubType.UDP = SyntheticsNetworkTestSubType("udp")
SyntheticsNetworkTestSubType.ICMP = SyntheticsNetworkTestSubType("icmp")
