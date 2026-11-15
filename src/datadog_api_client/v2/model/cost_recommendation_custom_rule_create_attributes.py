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
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_filter import CostRecommendationCustomRuleFilter
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_settings import (
        CostRecommendationCustomRuleSettings,
    )


class CostRecommendationCustomRuleCreateAttributes(ModelNormal):
    validations = {
        "name": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_filter import (
            CostRecommendationCustomRuleFilter,
        )
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_settings import (
            CostRecommendationCustomRuleSettings,
        )

        return {
            "enabled": (bool,),
            "filters": ([CostRecommendationCustomRuleFilter],),
            "name": (str,),
            "notes": (str,),
            "recommender_id": (str,),
            "settings": (CostRecommendationCustomRuleSettings,),
        }

    attribute_map = {
        "enabled": "enabled",
        "filters": "filters",
        "name": "name",
        "notes": "notes",
        "recommender_id": "recommender_id",
        "settings": "settings",
    }

    def __init__(
        self_,
        name: str,
        recommender_id: str,
        enabled: Union[bool, UnsetType] = unset,
        filters: Union[List[CostRecommendationCustomRuleFilter], UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        settings: Union[CostRecommendationCustomRuleSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a new custom recommendation rule.

        :param enabled: Whether the rule is applied when recommendations are generated. Defaults to ``true``.
        :type enabled: bool, optional

        :param filters: Tag filters that select the resources the rule applies to. An empty list selects every resource.
        :type filters: [CostRecommendationCustomRuleFilter], optional

        :param name: The name of the rule.
        :type name: str

        :param notes: Free-form notes, such as the reason for the customization.
        :type notes: str, optional

        :param recommender_id: The recommender to customize. It must be a recommender that supports custom rules.
        :type recommender_id: str

        :param settings: Setting overrides, keyed by setting name. Settings left out keep the recommender default. The accepted
            settings and their ranges depend on the recommender.
        :type settings: CostRecommendationCustomRuleSettings, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if filters is not unset:
            kwargs["filters"] = filters
        if notes is not unset:
            kwargs["notes"] = notes
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)

        self_.name = name
        self_.recommender_id = recommender_id
