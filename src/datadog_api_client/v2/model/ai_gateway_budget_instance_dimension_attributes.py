# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_budget_instance_dimension_value import (
        AiGatewayBudgetInstanceDimensionValue,
    )


class AiGatewayBudgetInstanceDimensionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_instance_dimension_value import (
            AiGatewayBudgetInstanceDimensionValue,
        )

        return {
            "budget_id": (UUID,),
            "dim": (str,),
            "restricted_details": (bool,),
            "truncated": (bool,),
            "values": ([AiGatewayBudgetInstanceDimensionValue],),
            "window_start": (datetime,),
        }

    attribute_map = {
        "budget_id": "budget_id",
        "dim": "dim",
        "restricted_details": "restricted_details",
        "truncated": "truncated",
        "values": "values",
        "window_start": "window_start",
    }

    def __init__(
        self_,
        budget_id: UUID,
        dim: str,
        restricted_details: bool,
        truncated: bool,
        values: List[AiGatewayBudgetInstanceDimensionValue],
        window_start: datetime,
        **kwargs,
    ):
        """
        Values of one budget split dimension.

        :param budget_id: Budget identifier.
        :type budget_id: UUID

        :param dim: Split dimension name, as used in ``split_dims`` and the ``split_dim`` filter.
        :type dim: str

        :param restricted_details: Whether identifying instance details were withheld. Aggregate totals still include restricted instances.
        :type restricted_details: bool

        :param truncated: Whether more values matched than were returned. Narrow the results with ``query`` or ``value`` to see them.
        :type truncated: bool

        :param values: Values of this dimension across matching instance counters, highest spend first and at most ``limit`` of them. Values are counted under every ``split_dim`` filter except the one for this dimension.
        :type values: [AiGatewayBudgetInstanceDimensionValue]

        :param window_start: Start of the accounting window.
        :type window_start: datetime
        """
        super().__init__(kwargs)

        self_.budget_id = budget_id
        self_.dim = dim
        self_.restricted_details = restricted_details
        self_.truncated = truncated
        self_.values = values
        self_.window_start = window_start
