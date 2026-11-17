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
    from datadog_api_client.v2.model.ai_gateway_budget_limit_mode import AiGatewayBudgetLimitMode


class AiGatewayBudgetReportingSummary(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_limit_mode import AiGatewayBudgetLimitMode

        return {
            "exceeded_capacity_count": (int,),
            "instance_count": (int,),
            "limit_mode": (AiGatewayBudgetLimitMode,),
            "over_warning_threshold_count": (int,),
            "total_capacity_microcents": (int,),
        }

    attribute_map = {
        "exceeded_capacity_count": "exceeded_capacity_count",
        "instance_count": "instance_count",
        "limit_mode": "limit_mode",
        "over_warning_threshold_count": "over_warning_threshold_count",
        "total_capacity_microcents": "total_capacity_microcents",
    }

    def __init__(
        self_,
        exceeded_capacity_count: int,
        instance_count: int,
        limit_mode: AiGatewayBudgetLimitMode,
        over_warning_threshold_count: int,
        total_capacity_microcents: int,
        **kwargs,
    ):
        """
        Health across all counters in the active accounting window. Includes hidden counters; contains no scope values or identities.

        :param exceeded_capacity_count: Number of counters at or above capacity.
        :type exceeded_capacity_count: int

        :param instance_count: Number of counters in the active window. Counters are created on first use.
        :type instance_count: int

        :param limit_mode: How the budget limit applies. ``shared`` is one limit for all matching traffic. ``per_instance`` is one
            limit for each counter of a template budget that splits by value.
        :type limit_mode: AiGatewayBudgetLimitMode

        :param over_warning_threshold_count: Number of counters at or above the warning threshold.
        :type over_warning_threshold_count: int

        :param total_capacity_microcents: Combined capacity of the counters in the active window, in microcents. A shared budget reports its configured limit before its first counter exists.
        :type total_capacity_microcents: int
        """
        super().__init__(kwargs)

        self_.exceeded_capacity_count = exceeded_capacity_count
        self_.instance_count = instance_count
        self_.limit_mode = limit_mode
        self_.over_warning_threshold_count = over_warning_threshold_count
        self_.total_capacity_microcents = total_capacity_microcents
