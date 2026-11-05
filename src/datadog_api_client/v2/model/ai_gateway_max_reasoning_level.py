# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayMaxReasoningLevel(ModelSimple):
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
    NONE: ClassVar["AiGatewayMaxReasoningLevel"]
    MINIMAL: ClassVar["AiGatewayMaxReasoningLevel"]
    LOW: ClassVar["AiGatewayMaxReasoningLevel"]
    MEDIUM: ClassVar["AiGatewayMaxReasoningLevel"]
    HIGH: ClassVar["AiGatewayMaxReasoningLevel"]
    XHIGH: ClassVar["AiGatewayMaxReasoningLevel"]
    MAX: ClassVar["AiGatewayMaxReasoningLevel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayMaxReasoningLevel.NONE = AiGatewayMaxReasoningLevel("none")
AiGatewayMaxReasoningLevel.MINIMAL = AiGatewayMaxReasoningLevel("minimal")
AiGatewayMaxReasoningLevel.LOW = AiGatewayMaxReasoningLevel("low")
AiGatewayMaxReasoningLevel.MEDIUM = AiGatewayMaxReasoningLevel("medium")
AiGatewayMaxReasoningLevel.HIGH = AiGatewayMaxReasoningLevel("high")
AiGatewayMaxReasoningLevel.XHIGH = AiGatewayMaxReasoningLevel("xhigh")
AiGatewayMaxReasoningLevel.MAX = AiGatewayMaxReasoningLevel("max")
