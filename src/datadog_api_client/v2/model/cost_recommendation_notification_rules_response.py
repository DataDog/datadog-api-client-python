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
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_data import (
        CostRecommendationNotificationRuleData,
    )


class CostRecommendationNotificationRulesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_data import (
            CostRecommendationNotificationRuleData,
        )

        return {
            "data": ([CostRecommendationNotificationRuleData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[CostRecommendationNotificationRuleData], **kwargs):
        """
        The recommendation notification rules of the organization.

        :param data: The notification rules.
        :type data: [CostRecommendationNotificationRuleData]
        """
        super().__init__(kwargs)

        self_.data = data
