# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostRecommendationCustomRuleFilterType(ModelSimple):
    """
    How the filter compares the tag. `is`, `is_not`, `contains`, `does_not_contain`, `like` (glob), and `not_like`
        compare the tag values with `values`. `all` matches resources that have the tag and `untagged` matches resources
        that do not, so both ignore `values`.

    :param value: Must be one of ["is", "is_not", "contains", "does_not_contain", "like", "not_like", "all", "untagged"].
    :type value: str
    """

    allowed_values = {
        "is",
        "is_not",
        "contains",
        "does_not_contain",
        "like",
        "not_like",
        "all",
        "untagged",
    }
    IS: ClassVar["CostRecommendationCustomRuleFilterType"]
    IS_NOT: ClassVar["CostRecommendationCustomRuleFilterType"]
    CONTAINS: ClassVar["CostRecommendationCustomRuleFilterType"]
    DOES_NOT_CONTAIN: ClassVar["CostRecommendationCustomRuleFilterType"]
    LIKE: ClassVar["CostRecommendationCustomRuleFilterType"]
    NOT_LIKE: ClassVar["CostRecommendationCustomRuleFilterType"]
    ALL: ClassVar["CostRecommendationCustomRuleFilterType"]
    UNTAGGED: ClassVar["CostRecommendationCustomRuleFilterType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostRecommendationCustomRuleFilterType.IS = CostRecommendationCustomRuleFilterType("is")
CostRecommendationCustomRuleFilterType.IS_NOT = CostRecommendationCustomRuleFilterType("is_not")
CostRecommendationCustomRuleFilterType.CONTAINS = CostRecommendationCustomRuleFilterType("contains")
CostRecommendationCustomRuleFilterType.DOES_NOT_CONTAIN = CostRecommendationCustomRuleFilterType("does_not_contain")
CostRecommendationCustomRuleFilterType.LIKE = CostRecommendationCustomRuleFilterType("like")
CostRecommendationCustomRuleFilterType.NOT_LIKE = CostRecommendationCustomRuleFilterType("not_like")
CostRecommendationCustomRuleFilterType.ALL = CostRecommendationCustomRuleFilterType("all")
CostRecommendationCustomRuleFilterType.UNTAGGED = CostRecommendationCustomRuleFilterType("untagged")
