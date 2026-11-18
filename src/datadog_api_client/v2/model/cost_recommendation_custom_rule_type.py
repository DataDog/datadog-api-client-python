# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostRecommendationCustomRuleType(ModelSimple):
    """
    Custom recommendation rule resource type.

    :param value: If omitted defaults to "custom_rules". Must be one of ["custom_rules"].
    :type value: str
    """

    allowed_values = {
        "custom_rules",
    }
    CUSTOM_RULES: ClassVar["CostRecommendationCustomRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostRecommendationCustomRuleType.CUSTOM_RULES = CostRecommendationCustomRuleType("custom_rules")
