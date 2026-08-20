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
    from datadog_api_client.v2.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
    from datadog_api_client.v2.model.product_analytics_base_query import ProductAnalyticsBaseQuery
    from datadog_api_client.v2.model.product_analytics_analytics_list_sort import ProductAnalyticsAnalyticsListSort
    from datadog_api_client.v2.model.product_analytics_event_query import ProductAnalyticsEventQuery
    from datadog_api_client.v2.model.product_analytics_occurrence_query import ProductAnalyticsOccurrenceQuery


class ProductAnalyticsAnalyticsListQuery(ModelNormal):
    validations = {
        "limit": {
            "inclusive_maximum": 1000,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
        from datadog_api_client.v2.model.product_analytics_base_query import ProductAnalyticsBaseQuery
        from datadog_api_client.v2.model.product_analytics_analytics_list_sort import ProductAnalyticsAnalyticsListSort

        return {
            "audience_filters": (ProductAnalyticsAudienceFilters,),
            "columns": ([str],),
            "limit": (int,),
            "query": (ProductAnalyticsBaseQuery,),
            "sort": (ProductAnalyticsAnalyticsListSort,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "columns": "columns",
        "limit": "limit",
        "query": "query",
        "sort": "sort",
    }

    def __init__(
        self_,
        query: Union[ProductAnalyticsBaseQuery, ProductAnalyticsEventQuery, ProductAnalyticsOccurrenceQuery],
        audience_filters: Union[ProductAnalyticsAudienceFilters, UnsetType] = unset,
        columns: Union[List[str], UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        sort: Union[ProductAnalyticsAnalyticsListSort, UnsetType] = unset,
        **kwargs,
    ):
        """
        The analytics list query definition. It selects the events to return with ``query`` , then
        chooses the columns on each event row, the sort applied to those rows, and a row limit.
        Unlike the scalar and timeseries queries, a list query returns raw event rows rather than
        aggregates, so it takes no compute or group-by rule.

        :param audience_filters: Audience filter definitions for targeting specific user segments.
        :type audience_filters: ProductAnalyticsAudienceFilters, optional

        :param columns: Attribute columns to include in each event row.
        :type columns: [str], optional

        :param limit: Maximum number of event rows to return.
        :type limit: int, optional

        :param query: A query definition discriminated by the ``data_source`` field.
            Use ``product_analytics`` for standard event queries, or
            ``product_analytics_occurrence`` for occurrence-filtered queries.
        :type query: ProductAnalyticsBaseQuery

        :param sort: The sort applied to the returned event rows.
        :type sort: ProductAnalyticsAnalyticsListSort, optional
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if columns is not unset:
            kwargs["columns"] = columns
        if limit is not unset:
            kwargs["limit"] = limit
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.query = query
