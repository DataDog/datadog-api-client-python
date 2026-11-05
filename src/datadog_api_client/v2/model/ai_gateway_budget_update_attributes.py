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
    from datadog_api_client.v2.model.ai_gateway_budget_enforcement import AiGatewayBudgetEnforcement


class AiGatewayBudgetUpdateAttributes(ModelNormal):
    validations = {
        "capacity_microcents": {
            "inclusive_minimum": 1,
        },
        "name": {
            "min_length": 1,
        },
        "reason": {
            "max_length": 1024,
        },
        "warning_threshold": {
            "inclusive_maximum": 1,
            "exclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_enforcement import AiGatewayBudgetEnforcement

        return {
            "apply_to_current_period": (bool,),
            "capacity_microcents": (int,),
            "enabled": (bool,),
            "enforcement": (AiGatewayBudgetEnforcement,),
            "name": (str,),
            "reason": (str,),
            "track_existing": (bool,),
            "warning_threshold": (float,),
        }

    attribute_map = {
        "apply_to_current_period": "apply_to_current_period",
        "capacity_microcents": "capacity_microcents",
        "enabled": "enabled",
        "enforcement": "enforcement",
        "name": "name",
        "reason": "reason",
        "track_existing": "track_existing",
        "warning_threshold": "warning_threshold",
    }

    def __init__(
        self_,
        apply_to_current_period: Union[bool, UnsetType] = unset,
        capacity_microcents: Union[int, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        enforcement: Union[AiGatewayBudgetEnforcement, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        reason: Union[str, UnsetType] = unset,
        track_existing: Union[bool, UnsetType] = unset,
        warning_threshold: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Mutable attributes of an AI Gateway budget.

        :param apply_to_current_period: Whether a capacity change also applies to the active accounting period. Requires capacity_microcents. Unsupported for template budgets.
        :type apply_to_current_period: bool, optional

        :param capacity_microcents: Default capacity for future accounting periods, in microcents.
        :type capacity_microcents: int, optional

        :param enabled: Whether the budget is enabled.
        :type enabled: bool, optional

        :param enforcement: Action taken when spend exceeds the budget.
        :type enforcement: AiGatewayBudgetEnforcement, optional

        :param name: Human-readable resource name.
        :type name: str, optional

        :param reason: Optional reason recorded with an active-period capacity adjustment.
        :type reason: str, optional

        :param track_existing: Initialize current-period spend from historical priced LLM Observability spans. Defaults to false. Unsupported for template budgets; failures can be retried with an update.
        :type track_existing: bool, optional

        :param warning_threshold: Fraction of capacity at which to issue a warning.
        :type warning_threshold: float, optional
        """
        if apply_to_current_period is not unset:
            kwargs["apply_to_current_period"] = apply_to_current_period
        if capacity_microcents is not unset:
            kwargs["capacity_microcents"] = capacity_microcents
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if enforcement is not unset:
            kwargs["enforcement"] = enforcement
        if name is not unset:
            kwargs["name"] = name
        if reason is not unset:
            kwargs["reason"] = reason
        if track_existing is not unset:
            kwargs["track_existing"] = track_existing
        if warning_threshold is not unset:
            kwargs["warning_threshold"] = warning_threshold
        super().__init__(kwargs)
