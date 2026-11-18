# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_data import CostRecommendationCustomRuleData


class CostRecommendationCustomRulesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_data import CostRecommendationCustomRuleData

        return {
            "data": ([CostRecommendationCustomRuleData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[CostRecommendationCustomRuleData], **kwargs):
        """
        The custom recommendation rules of the organization.

        :param data: The custom rules, ordered by recommender and then by priority.
        :type data: [CostRecommendationCustomRuleData]
        """
        super().__init__(kwargs)

        self_.data = data
