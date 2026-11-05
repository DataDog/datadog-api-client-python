# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
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


class AiGatewayBudgetAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_enforcement import AiGatewayBudgetEnforcement
        from datadog_api_client.v2.model.ai_gateway_budget_selector_entry import AiGatewayBudgetSelectorEntry
        from datadog_api_client.v2.model.ai_gateway_budget_tags import AiGatewayBudgetTags
        from datadog_api_client.v2.model.ai_gateway_budget_window_policy import AiGatewayBudgetWindowPolicy

        return {
            "capacity_microcents": (int,),
            "created_at": (datetime,),
            "created_by": (str,),
            "enabled": (bool,),
            "enforcement": (AiGatewayBudgetEnforcement,),
            "monitor_id": (int, none_type),
            "name": (str,),
            "scope_restricted": (bool,),
            "selector": ([AiGatewayBudgetSelectorEntry],),
            "tags": (AiGatewayBudgetTags,),
            "team_id": (UUID,),
            "updated_at": (datetime,),
            "user_id": (UUID,),
            "warning_threshold": (float,),
            "window_policy": (AiGatewayBudgetWindowPolicy,),
        }

    attribute_map = {
        "capacity_microcents": "capacity_microcents",
        "created_at": "created_at",
        "created_by": "created_by",
        "enabled": "enabled",
        "enforcement": "enforcement",
        "monitor_id": "monitor_id",
        "name": "name",
        "scope_restricted": "scope_restricted",
        "selector": "selector",
        "tags": "tags",
        "team_id": "team_id",
        "updated_at": "updated_at",
        "user_id": "user_id",
        "warning_threshold": "warning_threshold",
        "window_policy": "window_policy",
    }

    def __init__(
        self_,
        capacity_microcents: int,
        created_at: datetime,
        created_by: str,
        enabled: bool,
        enforcement: AiGatewayBudgetEnforcement,
        monitor_id: Union[int, none_type],
        name: str,
        scope_restricted: bool,
        tags: AiGatewayBudgetTags,
        updated_at: datetime,
        warning_threshold: float,
        window_policy: AiGatewayBudgetWindowPolicy,
        selector: Union[List[AiGatewayBudgetSelectorEntry], none_type, UnsetType] = unset,
        team_id: Union[UUID, UnsetType] = unset,
        user_id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        AI Gateway budget configuration and metadata.

        :param capacity_microcents: Budget capacity in microcents.
        :type capacity_microcents: int

        :param created_at: Time when the resource was created.
        :type created_at: datetime

        :param created_by: Identifier of the principal that created the resource.
        :type created_by: str

        :param enabled: Whether the resource is enabled.
        :type enabled: bool

        :param enforcement: Action taken when spend exceeds the budget.
        :type enforcement: AiGatewayBudgetEnforcement

        :param monitor_id: Datadog monitor ID provisioned for this budget. Null when monitor provisioning was skipped or failed.
        :type monitor_id: int, none_type

        :param name: Human-readable resource name.
        :type name: str

        :param scope_restricted: Whether provider or model scope metadata was withheld. Omit unchanged scope fields on an unrelated update to preserve their saved values.
        :type scope_restricted: bool

        :param selector: Dimension rules for a template budget. A nonempty selector creates independent counters for matched instances. Omit or pass an empty selector for a legacy fixed-scope budget.
        :type selector: [AiGatewayBudgetSelectorEntry], none_type, optional

        :param tags: Request tags that must match for the budget to apply.
        :type tags: AiGatewayBudgetTags

        :param team_id: Optional Datadog Team scope.
        :type team_id: UUID, optional

        :param updated_at: Time when the resource was last updated.
        :type updated_at: datetime

        :param user_id: User scope. Omitted when the budget is not user-scoped.
        :type user_id: UUID, optional

        :param warning_threshold: Fraction of capacity at which to issue a warning.
        :type warning_threshold: float

        :param window_policy: UTC accounting period for a budget.
        :type window_policy: AiGatewayBudgetWindowPolicy
        """
        if selector is not unset:
            kwargs["selector"] = selector
        if team_id is not unset:
            kwargs["team_id"] = team_id
        if user_id is not unset:
            kwargs["user_id"] = user_id
        super().__init__(kwargs)

        self_.capacity_microcents = capacity_microcents
        self_.created_at = created_at
        self_.created_by = created_by
        self_.enabled = enabled
        self_.enforcement = enforcement
        self_.monitor_id = monitor_id
        self_.name = name
        self_.scope_restricted = scope_restricted
        self_.tags = tags
        self_.updated_at = updated_at
        self_.warning_threshold = warning_threshold
        self_.window_policy = window_policy
