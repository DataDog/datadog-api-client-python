# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    UUID,
)


class AiGatewayBudgetInstancesSummaryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "budget_id": (UUID,),
            "exceeded_capacity_count": (int,),
            "instance_count": (int,),
            "over_warning_threshold_count": (int,),
            "restricted_details": (bool,),
            "total_spend_microcents": (int,),
            "window_start": (datetime,),
        }

    attribute_map = {
        "budget_id": "budget_id",
        "exceeded_capacity_count": "exceeded_capacity_count",
        "instance_count": "instance_count",
        "over_warning_threshold_count": "over_warning_threshold_count",
        "restricted_details": "restricted_details",
        "total_spend_microcents": "total_spend_microcents",
        "window_start": "window_start",
    }

    def __init__(
        self_,
        budget_id: UUID,
        exceeded_capacity_count: int,
        instance_count: int,
        over_warning_threshold_count: int,
        restricted_details: bool,
        total_spend_microcents: int,
        window_start: datetime,
        **kwargs,
    ):
        """
        Aggregate state across budget instance counters.

        :param budget_id: Budget identifier.
        :type budget_id: UUID

        :param exceeded_capacity_count: Number of instances at or above capacity.
        :type exceeded_capacity_count: int

        :param instance_count: Number of instance counters.
        :type instance_count: int

        :param over_warning_threshold_count: Number of instances at or above the warning threshold.
        :type over_warning_threshold_count: int

        :param restricted_details: Whether instances were withheld because their provider or model is hidden. Summary counts and totals exclude those instances.
        :type restricted_details: bool

        :param total_spend_microcents: Spend summed across all instances, in microcents.
        :type total_spend_microcents: int

        :param window_start: Start of the accounting window.
        :type window_start: datetime
        """
        super().__init__(kwargs)

        self_.budget_id = budget_id
        self_.exceeded_capacity_count = exceeded_capacity_count
        self_.instance_count = instance_count
        self_.over_warning_threshold_count = over_warning_threshold_count
        self_.restricted_details = restricted_details
        self_.total_spend_microcents = total_spend_microcents
        self_.window_start = window_start
