# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_actions import (
        CostRecommendationNotificationRuleMessageActions,
    )
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization_header import (
        CostRecommendationNotificationRuleMessageCustomizationHeader,
    )
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization_mode import (
        CostRecommendationNotificationRuleMessageCustomizationMode,
    )
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization_per_rec import (
        CostRecommendationNotificationRuleMessageCustomizationPerRec,
    )


class CostRecommendationNotificationRuleMessageCustomization(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_actions import (
            CostRecommendationNotificationRuleMessageActions,
        )
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization_header import (
            CostRecommendationNotificationRuleMessageCustomizationHeader,
        )
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization_mode import (
            CostRecommendationNotificationRuleMessageCustomizationMode,
        )
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization_per_rec import (
            CostRecommendationNotificationRuleMessageCustomizationPerRec,
        )

        return {
            "actions": (CostRecommendationNotificationRuleMessageActions,),
            "header": (CostRecommendationNotificationRuleMessageCustomizationHeader,),
            "include_tags": ([str],),
            "mode": (CostRecommendationNotificationRuleMessageCustomizationMode,),
            "per_rec": (CostRecommendationNotificationRuleMessageCustomizationPerRec,),
        }

    attribute_map = {
        "actions": "actions",
        "header": "header",
        "include_tags": "include_tags",
        "mode": "mode",
        "per_rec": "per_rec",
    }

    def __init__(
        self_,
        actions: Union[CostRecommendationNotificationRuleMessageActions, UnsetType] = unset,
        header: Union[CostRecommendationNotificationRuleMessageCustomizationHeader, UnsetType] = unset,
        include_tags: Union[List[str], UnsetType] = unset,
        mode: Union[CostRecommendationNotificationRuleMessageCustomizationMode, UnsetType] = unset,
        per_rec: Union[CostRecommendationNotificationRuleMessageCustomizationPerRec, UnsetType] = unset,
        **kwargs,
    ):
        """
        Which sections the digest shows. Sent as a whole: sections left out of a request use their defaults, which
        show everything.

        :param actions: Links the digest shows. ``view_in_ccm`` is the link to review the recommendations in Cloud Cost Management.
        :type actions: CostRecommendationNotificationRuleMessageActions, optional

        :param header: What the digest header shows.
        :type header: CostRecommendationNotificationRuleMessageCustomizationHeader, optional

        :param include_tags: Tag keys whose values are shown on each recommendation in the digest.
        :type include_tags: [str], optional

        :param mode: How the message is customized.
        :type mode: CostRecommendationNotificationRuleMessageCustomizationMode, optional

        :param per_rec: What each recommendation in the digest shows.
        :type per_rec: CostRecommendationNotificationRuleMessageCustomizationPerRec, optional
        """
        if actions is not unset:
            kwargs["actions"] = actions
        if header is not unset:
            kwargs["header"] = header
        if include_tags is not unset:
            kwargs["include_tags"] = include_tags
        if mode is not unset:
            kwargs["mode"] = mode
        if per_rec is not unset:
            kwargs["per_rec"] = per_rec
        super().__init__(kwargs)
