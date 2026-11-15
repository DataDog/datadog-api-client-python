# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_action import (
        CostRecommendationNotificationRuleMessageAction,
    )


class CostRecommendationNotificationRuleMessageActions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_action import (
            CostRecommendationNotificationRuleMessageAction,
        )

        return {
            "view_in_ccm": (CostRecommendationNotificationRuleMessageAction,),
        }

    attribute_map = {
        "view_in_ccm": "view_in_ccm",
    }

    def __init__(
        self_, view_in_ccm: Union[CostRecommendationNotificationRuleMessageAction, UnsetType] = unset, **kwargs
    ):
        """
        Links the digest shows. ``view_in_ccm`` is the link to review the recommendations in Cloud Cost Management.

        :param view_in_ccm: Where a message action appears.
        :type view_in_ccm: CostRecommendationNotificationRuleMessageAction, optional
        """
        if view_in_ccm is not unset:
            kwargs["view_in_ccm"] = view_in_ccm
        super().__init__(kwargs)
