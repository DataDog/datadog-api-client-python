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
    from datadog_api_client.v2.model.product_analytics_compute import ProductAnalyticsCompute
    from datadog_api_client.v2.model.product_analytics_group_by import ProductAnalyticsGroupBy
    from datadog_api_client.v2.model.product_analytics_base_query import ProductAnalyticsBaseQuery
    from datadog_api_client.v2.model.product_analytics_event_query import ProductAnalyticsEventQuery
    from datadog_api_client.v2.model.product_analytics_occurrence_query import ProductAnalyticsOccurrenceQuery


class ProductAnalyticsAnalyticsQuery(ModelNormal):
    validations = {
        "indexes": {
            "max_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
        from datadog_api_client.v2.model.product_analytics_compute import ProductAnalyticsCompute
        from datadog_api_client.v2.model.product_analytics_group_by import ProductAnalyticsGroupBy
        from datadog_api_client.v2.model.product_analytics_base_query import ProductAnalyticsBaseQuery

        return {
            "audience_filters": (ProductAnalyticsAudienceFilters,),
            "compute": (ProductAnalyticsCompute,),
            "group_by": ([ProductAnalyticsGroupBy],),
            "indexes": ([str],),
            "query": (ProductAnalyticsBaseQuery,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "compute": "compute",
        "group_by": "group_by",
        "indexes": "indexes",
        "query": "query",
    }

    def __init__(
        self_,
        compute: ProductAnalyticsCompute,
        query: Union[ProductAnalyticsBaseQuery, ProductAnalyticsEventQuery, ProductAnalyticsOccurrenceQuery],
        audience_filters: Union[ProductAnalyticsAudienceFilters, UnsetType] = unset,
        group_by: Union[List[ProductAnalyticsGroupBy], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The analytics query definition containing a base query, compute rule, and optional grouping.

        :param audience_filters: Audience filter definitions for targeting specific user segments.
        :type audience_filters: ProductAnalyticsAudienceFilters, optional

        :param compute: A compute rule for aggregating data.
        :type compute: ProductAnalyticsCompute

        :param group_by: Group-by rules for segmenting results.
        :type group_by: [ProductAnalyticsGroupBy], optional

        :param indexes: Restrict the query to specific indexes. Max 1 entry.
        :type indexes: [str], optional

        :param query: A query definition discriminated by the ``data_source`` field.
            Use ``product_analytics`` for standard event queries, or
            ``product_analytics_occurrence`` for occurrence-filtered queries.
        :type query: ProductAnalyticsBaseQuery
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if indexes is not unset:
            kwargs["indexes"] = indexes
        super().__init__(kwargs)

        self_.compute = compute
        self_.query = query
