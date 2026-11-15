# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_create_data import (
        CostRecommendationCustomRuleCreateData,
    )


class CostRecommendationCustomRuleCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_create_data import (
            CostRecommendationCustomRuleCreateData,
        )

        return {
            "data": (CostRecommendationCustomRuleCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CostRecommendationCustomRuleCreateData, **kwargs):
        """
        Request to create a custom recommendation rule.

        :param data: A new custom recommendation rule.
        :type data: CostRecommendationCustomRuleCreateData
        """
        super().__init__(kwargs)

        self_.data = data
