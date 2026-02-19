# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsNetworkTestRequestTCPMethod(ModelSimple):
    """
    For TCP tests, the TCP traceroute strategy.

    :param value: Must be one of ["prefer_sack", "syn", "sack"].
    :type value: str
    """

    allowed_values = {
        "prefer_sack",
        "syn",
        "sack",
    }
    PREFER_SACK: ClassVar["SyntheticsNetworkTestRequestTCPMethod"]
    SYN: ClassVar["SyntheticsNetworkTestRequestTCPMethod"]
    SACK: ClassVar["SyntheticsNetworkTestRequestTCPMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsNetworkTestRequestTCPMethod.PREFER_SACK = SyntheticsNetworkTestRequestTCPMethod("prefer_sack")
SyntheticsNetworkTestRequestTCPMethod.SYN = SyntheticsNetworkTestRequestTCPMethod("syn")
SyntheticsNetworkTestRequestTCPMethod.SACK = SyntheticsNetworkTestRequestTCPMethod("sack")
