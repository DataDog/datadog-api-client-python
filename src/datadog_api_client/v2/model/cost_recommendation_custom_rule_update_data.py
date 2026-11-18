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
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_update_attributes import (
        CostRecommendationCustomRuleUpdateAttributes,
    )
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_type import CostRecommendationCustomRuleType


class CostRecommendationCustomRuleUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_update_attributes import (
            CostRecommendationCustomRuleUpdateAttributes,
        )
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_type import CostRecommendationCustomRuleType

        return {
            "attributes": (CostRecommendationCustomRuleUpdateAttributes,),
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
        attributes: CostRecommendationCustomRuleUpdateAttributes,
        id: str,
        type: CostRecommendationCustomRuleType,
        **kwargs,
    ):
        """
        Changes to a custom recommendation rule.

        :param attributes: Attributes to change. Attributes left out keep their value. ``filters`` and ``settings`` replace the stored list
            and map when sent.
        :type attributes: CostRecommendationCustomRuleUpdateAttributes

        :param id: The ID of the custom rule. It must match the ID in the path.
        :type id: str

        :param type: Custom recommendation rule resource type.
        :type type: CostRecommendationCustomRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
