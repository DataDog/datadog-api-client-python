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
    from datadog_api_client.v2.model.query_sort_order import QuerySortOrder


class ProductAnalyticsGroupBySort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.query_sort_order import QuerySortOrder

        return {
            "aggregation": (str,),
            "metric": (str,),
            "order": (QuerySortOrder,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
        "order": "order",
    }

    def __init__(
        self_,
        aggregation: Union[str, UnsetType] = unset,
        metric: Union[str, UnsetType] = unset,
        order: Union[QuerySortOrder, UnsetType] = unset,
        **kwargs,
    ):
        """
        Sort configuration for group-by results.

        :param aggregation: The aggregation function to sort by.
        :type aggregation: str, optional

        :param metric: The metric to sort by.
        :type metric: str, optional

        :param order: Direction of sort.
        :type order: QuerySortOrder, optional
        """
        if aggregation is not unset:
            kwargs["aggregation"] = aggregation
        if metric is not unset:
            kwargs["metric"] = metric
        if order is not unset:
            kwargs["order"] = order
        super().__init__(kwargs)
