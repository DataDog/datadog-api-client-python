# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_budget_enforcement import AiGatewayBudgetEnforcement
    from datadog_api_client.v2.model.ai_gateway_budget_selector_entry import AiGatewayBudgetSelectorEntry
    from datadog_api_client.v2.model.ai_gateway_budget_tags import AiGatewayBudgetTags
    from datadog_api_client.v2.model.ai_gateway_budget_window_policy import AiGatewayBudgetWindowPolicy


class AiGatewayBudgetCreateAttributes(ModelNormal):
    validations = {
        "capacity_microcents": {
            "inclusive_minimum": 1,
        },
        "name": {
            "min_length": 1,
        },
        "warning_threshold": {
            "inclusive_maximum": 1,
            "exclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_enforcement import AiGatewayBudgetEnforcement
        from datadog_api_client.v2.model.ai_gateway_budget_selector_entry import AiGatewayBudgetSelectorEntry
        from datadog_api_client.v2.model.ai_gateway_budget_tags import AiGatewayBudgetTags
        from datadog_api_client.v2.model.ai_gateway_budget_window_policy import AiGatewayBudgetWindowPolicy

        return {
            "capacity_microcents": (int,),
            "enforcement": (AiGatewayBudgetEnforcement,),
            "name": (str,),
            "selector": ([AiGatewayBudgetSelectorEntry],),
            "tags": (AiGatewayBudgetTags,),
            "team_id": (UUID,),
            "track_existing": (bool,),
            "user_id": (UUID,),
            "warning_threshold": (float,),
            "window_policy": (AiGatewayBudgetWindowPolicy,),
        }

    attribute_map = {
        "capacity_microcents": "capacity_microcents",
        "enforcement": "enforcement",
        "name": "name",
        "selector": "selector",
        "tags": "tags",
        "team_id": "team_id",
        "track_existing": "track_existing",
        "user_id": "user_id",
        "warning_threshold": "warning_threshold",
        "window_policy": "window_policy",
    }

    def __init__(
        self_,
        capacity_microcents: int,
        enforcement: AiGatewayBudgetEnforcement,
        name: str,
        window_policy: AiGatewayBudgetWindowPolicy,
        selector: Union[List[AiGatewayBudgetSelectorEntry], none_type, UnsetType] = unset,
        tags: Union[AiGatewayBudgetTags, UnsetType] = unset,
        team_id: Union[UUID, UnsetType] = unset,
        track_existing: Union[bool, UnsetType] = unset,
        user_id: Union[UUID, UnsetType] = unset,
        warning_threshold: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes used to create an AI Gateway budget.

        :param capacity_microcents: Budget capacity in microcents.
        :type capacity_microcents: int

        :param enforcement: Action taken when spend exceeds the budget.
        :type enforcement: AiGatewayBudgetEnforcement

        :param name: Human-readable resource name.
        :type name: str

        :param selector: Dimension rules for a template budget. A nonempty selector creates independent counters for matched instances. Omit or pass an empty selector for a legacy fixed-scope budget.
        :type selector: [AiGatewayBudgetSelectorEntry], none_type, optional

        :param tags: Request tags that must match for the budget to apply.
        :type tags: AiGatewayBudgetTags, optional

        :param team_id: Optional Datadog Team scope.
        :type team_id: UUID, optional

        :param track_existing: Initialize current-period spend from historical priced LLM Observability spans. Defaults to false. Unsupported for template budgets; failures can be retried with an update.
        :type track_existing: bool, optional

        :param user_id: Optional user scope.
        :type user_id: UUID, optional

        :param warning_threshold: Fraction of capacity at which to issue a warning.
        :type warning_threshold: float, optional

        :param window_policy: UTC accounting period for a budget.
        :type window_policy: AiGatewayBudgetWindowPolicy
        """
        if selector is not unset:
            kwargs["selector"] = selector
        if tags is not unset:
            kwargs["tags"] = tags
        if team_id is not unset:
            kwargs["team_id"] = team_id
        if track_existing is not unset:
            kwargs["track_existing"] = track_existing
        if user_id is not unset:
            kwargs["user_id"] = user_id
        if warning_threshold is not unset:
            kwargs["warning_threshold"] = warning_threshold
        super().__init__(kwargs)

        self_.capacity_microcents = capacity_microcents
        self_.enforcement = enforcement
        self_.name = name
        self_.window_policy = window_policy
