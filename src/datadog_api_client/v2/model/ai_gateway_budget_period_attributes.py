# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    UUID,
)


class AiGatewayBudgetPeriodAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "budget_id": (UUID,),
            "current_spend_microcents": (int,),
            "default_capacity_microcents": (int,),
            "effective_capacity_microcents": (int,),
            "monitor_id": (int, none_type),
            "window_end": (datetime,),
            "window_start": (datetime,),
        }

    attribute_map = {
        "budget_id": "budget_id",
        "current_spend_microcents": "current_spend_microcents",
        "default_capacity_microcents": "default_capacity_microcents",
        "effective_capacity_microcents": "effective_capacity_microcents",
        "monitor_id": "monitor_id",
        "window_end": "window_end",
        "window_start": "window_start",
    }

    def __init__(
        self_,
        budget_id: UUID,
        current_spend_microcents: int,
        default_capacity_microcents: int,
        effective_capacity_microcents: int,
        monitor_id: Union[int, none_type],
        window_end: datetime,
        window_start: datetime,
        **kwargs,
    ):
        """
        Accounting state enforced for an AI Gateway budget's active period.

        :param budget_id: Budget resource identifier.
        :type budget_id: UUID

        :param current_spend_microcents: Spend currently counted against the active accounting period.
        :type current_spend_microcents: int

        :param default_capacity_microcents: Capacity that new accounting periods inherit from the budget definition.
        :type default_capacity_microcents: int

        :param effective_capacity_microcents: Capacity enforced for the active accounting period.
        :type effective_capacity_microcents: int

        :param monitor_id: Datadog monitor ID provisioned for this budget. Null when monitor provisioning was skipped or failed.
        :type monitor_id: int, none_type

        :param window_end: End of the active accounting window.
        :type window_end: datetime

        :param window_start: Start of the active accounting window.
        :type window_start: datetime
        """
        super().__init__(kwargs)

        self_.budget_id = budget_id
        self_.current_spend_microcents = current_spend_microcents
        self_.default_capacity_microcents = default_capacity_microcents
        self_.effective_capacity_microcents = effective_capacity_microcents
        self_.monitor_id = monitor_id
        self_.window_end = window_end
        self_.window_start = window_start
