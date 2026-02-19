# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsNetworkAssertionLatencyType(ModelSimple):
    """
    Type of the latency assertion.

    :param value: If omitted defaults to "latency". Must be one of ["latency"].
    :type value: str
    """

    allowed_values = {
        "latency",
    }
    LATENCY: ClassVar["SyntheticsNetworkAssertionLatencyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsNetworkAssertionLatencyType.LATENCY = SyntheticsNetworkAssertionLatencyType("latency")
