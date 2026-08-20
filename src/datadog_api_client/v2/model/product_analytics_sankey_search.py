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


class ProductAnalyticsSankeySearch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
        from datadog_api_client.v2.model.product_analytics_join_keys import ProductAnalyticsJoinKeys

        return {
            "audience_filters": (ProductAnalyticsAudienceFilters,),
            "join_keys": (ProductAnalyticsJoinKeys,),
            "query": (str,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "join_keys": "join_keys",
        "query": "query",
    }

    def __init__(
        self_,
        audience_filters: Union[ProductAnalyticsAudienceFilters, UnsetType] = unset,
        join_keys: Union[ProductAnalyticsJoinKeys, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Selects the sessions a Sankey diagram is built from.

        :param audience_filters: Audience filter definitions for targeting specific user segments.
        :type audience_filters: ProductAnalyticsAudienceFilters, optional

        :param join_keys: Identity join keys used to stitch events belonging to the same user or session.
        :type join_keys: ProductAnalyticsJoinKeys, optional

        :param query: Datadog search query restricting the events considered.
        :type query: str, optional
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if join_keys is not unset:
            kwargs["join_keys"] = join_keys
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)
