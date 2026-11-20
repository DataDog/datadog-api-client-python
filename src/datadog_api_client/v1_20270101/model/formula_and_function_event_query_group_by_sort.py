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
    from datadog_api_client.v1_20270101.model.events_aggregator import EventsAggregator
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder


class FormulaAndFunctionEventQueryGroupBySort(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_aggregator import EventsAggregator
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder

        return {
            "aggregation": (EventsAggregator,),
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
        aggregation: Union[EventsAggregator, str],
        metric: Union[str, UnsetType] = unset,
        order: Union[QuerySortOrder, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: EventsAggregator

        :param metric: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric: str, optional

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder, optional
        """
        if metric is not unset:
            kwargs["metric"] = metric
        if order is not unset:
            kwargs["order"] = order
        super().__init__(kwargs)

        self_.aggregation = aggregation
