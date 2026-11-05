# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelReasoningControlType(ModelSimple):
    """
    Reasoning-control mechanism.

    :param value: Must be one of ["toggle", "effort", "budget_tokens"].
    :type value: str
    """

    allowed_values = {
        "toggle",
        "effort",
        "budget_tokens",
    }
    TOGGLE: ClassVar["AiGatewayModelReasoningControlType"]
    EFFORT: ClassVar["AiGatewayModelReasoningControlType"]
    BUDGET_TOKENS: ClassVar["AiGatewayModelReasoningControlType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelReasoningControlType.TOGGLE = AiGatewayModelReasoningControlType("toggle")
AiGatewayModelReasoningControlType.EFFORT = AiGatewayModelReasoningControlType("effort")
AiGatewayModelReasoningControlType.BUDGET_TOKENS = AiGatewayModelReasoningControlType("budget_tokens")
