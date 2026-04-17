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
    from datadog_api_client.v2.model.metrics_aggregator import MetricsAggregator
    from datadog_api_client.v2.model.container_data_source import ContainerDataSource
    from datadog_api_client.v2.model.query_sort_order import QuerySortOrder


class ContainerScalarQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metrics_aggregator import MetricsAggregator
        from datadog_api_client.v2.model.container_data_source import ContainerDataSource
        from datadog_api_client.v2.model.query_sort_order import QuerySortOrder

        return {
            "aggregator": (MetricsAggregator,),
            "data_source": (ContainerDataSource,),
            "is_normalized_cpu": (bool,),
            "limit": (int,),
            "metric": (str,),
            "name": (str,),
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
        "sort": "sort",
        "tag_filters": "tag_filters",
        "text_filter": "text_filter",
    }

    def __init__(
        self_,
        data_source: ContainerDataSource,
        metric: str,
        name: str,
        aggregator: Union[MetricsAggregator, UnsetType] = unset,
        is_normalized_cpu: Union[bool, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        sort: Union[QuerySortOrder, UnsetType] = unset,
        tag_filters: Union[List[str], UnsetType] = unset,
        text_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A query for container-level metrics such as CPU and memory usage.

        :param aggregator: The type of aggregation that can be performed on metrics-based queries.
        :type aggregator: MetricsAggregator, optional

        :param data_source: A data source for container-level infrastructure metrics.
        :type data_source: ContainerDataSource

        :param is_normalized_cpu: Whether CPU metrics should be normalized by core count.
        :type is_normalized_cpu: bool, optional

        :param limit: Maximum number of results to return.
        :type limit: int, optional

        :param metric: The container metric to query.
        :type metric: str

        :param name: The variable name for use in formulas.
        :type name: str

        :param sort: Direction of sort.
        :type sort: QuerySortOrder, optional

        :param tag_filters: Tag filters to narrow down containers.
        :type tag_filters: [str], optional

        :param text_filter: A full-text search filter to match container names.
        :type text_filter: str, optional
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if is_normalized_cpu is not unset:
            kwargs["is_normalized_cpu"] = is_normalized_cpu
        if limit is not unset:
            kwargs["limit"] = limit
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
