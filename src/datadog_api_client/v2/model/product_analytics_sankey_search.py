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
    from datadog_api_client.v2.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
    from datadog_api_client.v2.model.product_analytics_join_keys import ProductAnalyticsJoinKeys
    from datadog_api_client.v2.model.product_analytics_occurrence_filter import ProductAnalyticsOccurrenceFilter


class ProductAnalyticsSankeySearch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
        from datadog_api_client.v2.model.product_analytics_join_keys import ProductAnalyticsJoinKeys
        from datadog_api_client.v2.model.product_analytics_occurrence_filter import ProductAnalyticsOccurrenceFilter

        return {
            "audience_filters": (ProductAnalyticsAudienceFilters,),
            "join_keys": (ProductAnalyticsJoinKeys,),
            "occurrences": (ProductAnalyticsOccurrenceFilter,),
            "query": (str,),
            "subquery_id": (str,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "join_keys": "join_keys",
        "occurrences": "occurrences",
        "query": "query",
        "subquery_id": "subquery_id",
    }

    def __init__(
        self_,
        query: str,
        audience_filters: Union[ProductAnalyticsAudienceFilters, UnsetType] = unset,
        join_keys: Union[ProductAnalyticsJoinKeys, UnsetType] = unset,
        occurrences: Union[ProductAnalyticsOccurrenceFilter, UnsetType] = unset,
        subquery_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Search parameters for a Sankey query.

        :param audience_filters: Audience filter definitions for targeting specific user segments.
        :type audience_filters: ProductAnalyticsAudienceFilters, optional

        :param join_keys: Join key configuration for correlating events.
        :type join_keys: ProductAnalyticsJoinKeys, optional

        :param occurrences: Filter for occurrence-based queries.
        :type occurrences: ProductAnalyticsOccurrenceFilter, optional

        :param query: The search query. Cannot be empty.
        :type query: str

        :param subquery_id:
        :type subquery_id: str, optional
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if join_keys is not unset:
            kwargs["join_keys"] = join_keys
        if occurrences is not unset:
            kwargs["occurrences"] = occurrences
        if subquery_id is not unset:
            kwargs["subquery_id"] = subquery_id
        super().__init__(kwargs)

        self_.query = query
