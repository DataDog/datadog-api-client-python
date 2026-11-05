# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    UUID,
)


class AiGatewayBudgetInstanceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "budget_id": (UUID,),
            "effective_capacity_microcents": (int,),
            "instance_key": (str,),
            "modified_at": (datetime,),
            "spend_microcents": (int,),
            "split_dims": ({str: (str,)},),
            "window_start": (datetime,),
        }

    attribute_map = {
        "budget_id": "budget_id",
        "effective_capacity_microcents": "effective_capacity_microcents",
        "instance_key": "instance_key",
        "modified_at": "modified_at",
        "spend_microcents": "spend_microcents",
        "split_dims": "split_dims",
        "window_start": "window_start",
    }

    def __init__(
        self_,
        budget_id: UUID,
        effective_capacity_microcents: int,
        instance_key: str,
        modified_at: datetime,
        spend_microcents: int,
        split_dims: Dict[str, str],
        window_start: datetime,
        **kwargs,
    ):
        """
        One budget instance counter.

        :param budget_id: Budget identifier.
        :type budget_id: UUID

        :param effective_capacity_microcents: Capacity enforced for this instance, in microcents.
        :type effective_capacity_microcents: int

        :param instance_key: Opaque canonical counter key. Empty for legacy pooled counters.
        :type instance_key: str

        :param modified_at: Time the instance counter was last modified.
        :type modified_at: datetime

        :param spend_microcents: Spend counted against this instance, in microcents.
        :type spend_microcents: int

        :param split_dims: Dimension values decoded from instance_key. User and Team values are raw UUIDs.
        :type split_dims: {str: (str,)}

        :param window_start: Start of the accounting window.
        :type window_start: datetime
        """
        super().__init__(kwargs)

        self_.budget_id = budget_id
        self_.effective_capacity_microcents = effective_capacity_microcents
        self_.instance_key = instance_key
        self_.modified_at = modified_at
        self_.spend_microcents = spend_microcents
        self_.split_dims = split_dims
        self_.window_start = window_start
