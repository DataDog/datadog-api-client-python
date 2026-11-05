# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayRoutingReasoningLevel(ModelSimple):
    """
    Optional reasoning effort preference for this model destination. Must be supported by the selected model and provider. For provider "*", every eligible provider must support the level. An explicit value overrides the request's reasoning setting, subject to model-group policy. Omitted or null preserves request and provider behavior; none is an explicit level, not the default. Omitted or null clears an override on full replacement. Routing-rule references cannot set this field; each referenced model destination owns its override. If an override cannot be applied at runtime, the gateway keeps the destination and restores the caller's original reasoning settings, or preserves the provider default when omitted. It rechecks all applicable route and model-group policies against those settings before sending. Model-group max_reasoning_level enforces hard limits; the override is not an additional cap. Normal fallback applies if governance denies the resulting request or the destination cannot otherwise serve it. Metrics and span tags record the override outcome and incompatibility reason. When response headers have not already been committed, `X-Ai-Gateway-Reasoning-Override` reports applied or not_applied for the returned attempt, and `X-Ai-Gateway-Reasoning-Override-Reason` reports the reason when not applied.

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
    NONE: ClassVar["AiGatewayRoutingReasoningLevel"]
    MINIMAL: ClassVar["AiGatewayRoutingReasoningLevel"]
    LOW: ClassVar["AiGatewayRoutingReasoningLevel"]
    MEDIUM: ClassVar["AiGatewayRoutingReasoningLevel"]
    HIGH: ClassVar["AiGatewayRoutingReasoningLevel"]
    XHIGH: ClassVar["AiGatewayRoutingReasoningLevel"]
    MAX: ClassVar["AiGatewayRoutingReasoningLevel"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayRoutingReasoningLevel.NONE = AiGatewayRoutingReasoningLevel("none")
AiGatewayRoutingReasoningLevel.MINIMAL = AiGatewayRoutingReasoningLevel("minimal")
AiGatewayRoutingReasoningLevel.LOW = AiGatewayRoutingReasoningLevel("low")
AiGatewayRoutingReasoningLevel.MEDIUM = AiGatewayRoutingReasoningLevel("medium")
AiGatewayRoutingReasoningLevel.HIGH = AiGatewayRoutingReasoningLevel("high")
AiGatewayRoutingReasoningLevel.XHIGH = AiGatewayRoutingReasoningLevel("xhigh")
AiGatewayRoutingReasoningLevel.MAX = AiGatewayRoutingReasoningLevel("max")
