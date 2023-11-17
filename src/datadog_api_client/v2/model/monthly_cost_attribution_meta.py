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
    from datadog_api_client.v2.model.cost_attribution_aggregates_body import CostAttributionAggregatesBody
    from datadog_api_client.v2.model.monthly_cost_attribution_pagination import MonthlyCostAttributionPagination


class MonthlyCostAttributionMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_attribution_aggregates_body import CostAttributionAggregatesBody
        from datadog_api_client.v2.model.monthly_cost_attribution_pagination import MonthlyCostAttributionPagination

        return {
            "aggregates": ([CostAttributionAggregatesBody],),
            "pagination": (MonthlyCostAttributionPagination,),
        }

    attribute_map = {
        "aggregates": "aggregates",
        "pagination": "pagination",
    }

    def __init__(
        self_,
        aggregates: Union[List[CostAttributionAggregatesBody], UnsetType] = unset,
        pagination: Union[MonthlyCostAttributionPagination, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object containing document metadata.

        :param aggregates: An array of available aggregates.
        :type aggregates: [CostAttributionAggregatesBody], optional

        :param pagination: The metadata for the current pagination.
        :type pagination: MonthlyCostAttributionPagination, optional
        """
        if aggregates is not unset:
            kwargs["aggregates"] = aggregates
        if pagination is not unset:
            kwargs["pagination"] = pagination
        super().__init__(kwargs)
