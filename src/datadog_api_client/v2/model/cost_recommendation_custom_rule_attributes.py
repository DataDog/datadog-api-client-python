# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_filter import CostRecommendationCustomRuleFilter
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_settings import (
        CostRecommendationCustomRuleSettings,
    )


class CostRecommendationCustomRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_filter import (
            CostRecommendationCustomRuleFilter,
        )
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_settings import (
            CostRecommendationCustomRuleSettings,
        )

        return {
            "cloud_provider": (str,),
            "created_at": (datetime,),
            "created_by": (str,),
            "enabled": (bool,),
            "filters": ([CostRecommendationCustomRuleFilter],),
            "modified_at": (datetime,),
            "modified_by": (str,),
            "name": (str,),
            "notes": (str,),
            "priority": (int,),
            "recommender_id": (str,),
            "settings": (CostRecommendationCustomRuleSettings,),
        }

    attribute_map = {
        "cloud_provider": "cloud_provider",
        "created_at": "created_at",
        "created_by": "created_by",
        "enabled": "enabled",
        "filters": "filters",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "name": "name",
        "notes": "notes",
        "priority": "priority",
        "recommender_id": "recommender_id",
        "settings": "settings",
    }

    def __init__(
        self_,
        cloud_provider: str,
        created_at: datetime,
        created_by: str,
        enabled: bool,
        filters: List[CostRecommendationCustomRuleFilter],
        modified_at: datetime,
        modified_by: str,
        name: str,
        notes: str,
        priority: int,
        recommender_id: str,
        settings: CostRecommendationCustomRuleSettings,
        **kwargs,
    ):
        """
        Attributes of a custom recommendation rule.

        :param cloud_provider: The cloud provider of the recommender, such as ``aws`` , ``azure`` , or ``gcp``.
        :type cloud_provider: str

        :param created_at: When the rule was created.
        :type created_at: datetime

        :param created_by: The UUID of the user who created the rule.
        :type created_by: str

        :param enabled: Whether the rule is applied when recommendations are generated.
        :type enabled: bool

        :param filters: Tag filters that select the resources the rule applies to. An empty list selects every resource.
        :type filters: [CostRecommendationCustomRuleFilter]

        :param modified_at: When the rule was last modified.
        :type modified_at: datetime

        :param modified_by: The UUID of the user who last modified the rule.
        :type modified_by: str

        :param name: The name of the rule.
        :type name: str

        :param notes: Free-form notes, such as the reason for the customization.
        :type notes: str

        :param priority: The order in which the rules of a recommender are evaluated, lowest first. It is assigned when the rule is created.
        :type priority: int

        :param recommender_id: The recommender the rule customizes.
        :type recommender_id: str

        :param settings: Setting overrides, keyed by setting name. Settings left out keep the recommender default. The accepted
            settings and their ranges depend on the recommender.
        :type settings: CostRecommendationCustomRuleSettings
        """
        super().__init__(kwargs)

        self_.cloud_provider = cloud_provider
        self_.created_at = created_at
        self_.created_by = created_by
        self_.enabled = enabled
        self_.filters = filters
        self_.modified_at = modified_at
        self_.modified_by = modified_by
        self_.name = name
        self_.notes = notes
        self_.priority = priority
        self_.recommender_id = recommender_id
        self_.settings = settings
