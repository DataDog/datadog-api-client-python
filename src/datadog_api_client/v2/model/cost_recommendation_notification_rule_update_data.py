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
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_update_attributes import (
        CostRecommendationNotificationRuleUpdateAttributes,
    )
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_type import (
        CostRecommendationNotificationRuleType,
    )


class CostRecommendationNotificationRuleUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_update_attributes import (
            CostRecommendationNotificationRuleUpdateAttributes,
        )
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_type import (
            CostRecommendationNotificationRuleType,
        )

        return {
            "attributes": (CostRecommendationNotificationRuleUpdateAttributes,),
            "id": (str,),
            "type": (CostRecommendationNotificationRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CostRecommendationNotificationRuleUpdateAttributes,
        id: str,
        type: CostRecommendationNotificationRuleType,
        **kwargs,
    ):
        """
        Changes to a recommendation notification rule.

        :param attributes: Attributes to change. Attributes left out keep their value; ``mention_targets`` and ``message_customization``
            replace the stored value when sent.
        :type attributes: CostRecommendationNotificationRuleUpdateAttributes

        :param id: The ID of the notification rule. It must match the ID in the path.
        :type id: str

        :param type: Recommendation notification rule resource type.
        :type type: CostRecommendationNotificationRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
