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
    from datadog_api_client.v1_20270101.model.dataset_sort20270101_aggregation import DatasetSort20270101Aggregation
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
    from datadog_api_client.v1_20270101.model.events_aggregator import EventsAggregator


class DatasetSort(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dataset_sort20270101_aggregation import DatasetSort20270101Aggregation
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder

        return {
            "aggregation": (DatasetSort20270101Aggregation,),
            "column": (str,),
            "order": (QuerySortOrder,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "column": "column",
        "order": "order",
    }

    def __init__(
        self_,
        aggregation: Union[DatasetSort20270101Aggregation, str, EventsAggregator],
        order: QuerySortOrder,
        column: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: DatasetSort20270101Aggregation

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str, optional

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder
        """
        if column is not unset:
            kwargs["column"] = column
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.order = order
