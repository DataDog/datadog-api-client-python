# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ArbitraryRuleResponseDataAttributesRuleCategory(ModelSimple):
    """
    Rule category. Omitted for custom rules.

    :param value: Must be one of ["custom", "ai_gateway"].
    :type value: str
    """

    allowed_values = {
        "custom",
        "ai_gateway",
    }
    CUSTOM: ClassVar["ArbitraryRuleResponseDataAttributesRuleCategory"]
    AI_GATEWAY: ClassVar["ArbitraryRuleResponseDataAttributesRuleCategory"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ArbitraryRuleResponseDataAttributesRuleCategory.CUSTOM = ArbitraryRuleResponseDataAttributesRuleCategory("custom")
ArbitraryRuleResponseDataAttributesRuleCategory.AI_GATEWAY = ArbitraryRuleResponseDataAttributesRuleCategory(
    "ai_gateway"
)
