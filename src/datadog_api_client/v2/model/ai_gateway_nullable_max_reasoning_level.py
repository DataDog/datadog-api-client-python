# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayNullableMaxReasoningLevel(ModelSimple):
    """
    Maximum reasoning level permitted by a model group.

    :param value: Must be one of ["none", "minimal", "low", "medium", "high", "xhigh", "max"].
    :type value: str
    """

    allowed_values = {
        "none",
        "minimal",
        "low",
        "medium",
        "high",
        "xhigh",
        "max",
    }
    NONE: ClassVar["AiGatewayNullableMaxReasoningLevel"]
    MINIMAL: ClassVar["AiGatewayNullableMaxReasoningLevel"]
    LOW: ClassVar["AiGatewayNullableMaxReasoningLevel"]
    MEDIUM: ClassVar["AiGatewayNullableMaxReasoningLevel"]
    HIGH: ClassVar["AiGatewayNullableMaxReasoningLevel"]
    XHIGH: ClassVar["AiGatewayNullableMaxReasoningLevel"]
    MAX: ClassVar["AiGatewayNullableMaxReasoningLevel"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayNullableMaxReasoningLevel.NONE = AiGatewayNullableMaxReasoningLevel("none")
AiGatewayNullableMaxReasoningLevel.MINIMAL = AiGatewayNullableMaxReasoningLevel("minimal")
AiGatewayNullableMaxReasoningLevel.LOW = AiGatewayNullableMaxReasoningLevel("low")
AiGatewayNullableMaxReasoningLevel.MEDIUM = AiGatewayNullableMaxReasoningLevel("medium")
AiGatewayNullableMaxReasoningLevel.HIGH = AiGatewayNullableMaxReasoningLevel("high")
AiGatewayNullableMaxReasoningLevel.XHIGH = AiGatewayNullableMaxReasoningLevel("xhigh")
AiGatewayNullableMaxReasoningLevel.MAX = AiGatewayNullableMaxReasoningLevel("max")
