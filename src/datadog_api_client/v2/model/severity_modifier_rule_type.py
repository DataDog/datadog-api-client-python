# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SeverityModifierRuleType(ModelSimple):
    """
    The JSON:API type for severity modifier rules.

    :param value: If omitted defaults to "severity_modifier_rules". Must be one of ["severity_modifier_rules"].
    :type value: str
    """

    allowed_values = {
        "severity_modifier_rules",
    }
    SEVERITY_MODIFIER_RULES: ClassVar["SeverityModifierRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SeverityModifierRuleType.SEVERITY_MODIFIER_RULES = SeverityModifierRuleType("severity_modifier_rules")
