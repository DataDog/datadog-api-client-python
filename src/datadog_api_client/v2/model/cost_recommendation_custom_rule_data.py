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
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_attributes import (
        CostRecommendationCustomRuleAttributes,
    )
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_type import CostRecommendationCustomRuleType


class CostRecommendationCustomRuleData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_attributes import (
            CostRecommendationCustomRuleAttributes,
        )
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_type import CostRecommendationCustomRuleType

        return {
            "attributes": (CostRecommendationCustomRuleAttributes,),
            "id": (str,),
            "type": (CostRecommendationCustomRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CostRecommendationCustomRuleAttributes,
        id: str,
        type: CostRecommendationCustomRuleType,
        **kwargs,
    ):
        """
        A custom recommendation rule.

        :param attributes: Attributes of a custom recommendation rule.
        :type attributes: CostRecommendationCustomRuleAttributes

        :param id: The ID of the custom rule.
        :type id: str

        :param type: Custom recommendation rule resource type.
        :type type: CostRecommendationCustomRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
