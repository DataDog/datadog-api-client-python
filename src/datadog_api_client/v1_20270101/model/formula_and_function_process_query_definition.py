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
    from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
    from datadog_api_client.v1_20270101.model.formula_and_function_process_query_data_source import (
        FormulaAndFunctionProcessQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder


class FormulaAndFunctionProcessQueryDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
        from datadog_api_client.v1_20270101.model.formula_and_function_process_query_data_source import (
            FormulaAndFunctionProcessQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder

        return {
            "aggregator": (ScalarAggregator,),
            "data_source": (FormulaAndFunctionProcessQueryDataSource,),
            "is_normalized_cpu": (bool,),
            "limit": (float,),
            "metric": (str,),
            "name": (str,),
            "query_filter": (str,),
            "sort": (QuerySortOrder,),
            "tag_filters": ([str],),
            "text_filter": (str,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "data_source": "data_source",
        "is_normalized_cpu": "is_normalized_cpu",
        "limit": "limit",
        "metric": "metric",
        "name": "name",
        "query_filter": "query_filter",
        "sort": "sort",
        "tag_filters": "tag_filters",
        "text_filter": "text_filter",
    }

    def __init__(
        self_,
        data_source: FormulaAndFunctionProcessQueryDataSource,
        metric: str,
        name: str,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        is_normalized_cpu: Union[bool, UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        sort: Union[QuerySortOrder, UnsetType] = unset,
        tag_filters: Union[List[str], UnsetType] = unset,
        text_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaAndFunctionProcessQueryDataSource

        :param is_normalized_cpu: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_normalized_cpu: bool, optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param metric: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: QuerySortOrder, optional

        :param tag_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type tag_filters: [str], optional

        :param text_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_filter: str, optional
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if is_normalized_cpu is not unset:
            kwargs["is_normalized_cpu"] = is_normalized_cpu
        if limit is not unset:
            kwargs["limit"] = limit
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        if sort is not unset:
            kwargs["sort"] = sort
        if tag_filters is not unset:
            kwargs["tag_filters"] = tag_filters
        if text_filter is not unset:
            kwargs["text_filter"] = text_filter
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.metric = metric
        self_.name = name
