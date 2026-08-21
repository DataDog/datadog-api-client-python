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
    from datadog_api_client.v2.model.product_analytics_journey_audience_filters import (
        ProductAnalyticsJourneyAudienceFilters,
    )
    from datadog_api_client.v2.model.product_analytics_journey_search_graph_filter import (
        ProductAnalyticsJourneySearchGraphFilter,
    )


class ProductAnalyticsJourneySearchFilters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_audience_filters import (
            ProductAnalyticsJourneyAudienceFilters,
        )
        from datadog_api_client.v2.model.product_analytics_journey_search_graph_filter import (
            ProductAnalyticsJourneySearchGraphFilter,
        )

        return {
            "audience_filters": (ProductAnalyticsJourneyAudienceFilters,),
            "graph_filters": ([ProductAnalyticsJourneySearchGraphFilter],),
            "string_filter": (str,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "graph_filters": "graph_filters",
        "string_filter": "string_filter",
    }

    def __init__(
        self_,
        audience_filters: Union[ProductAnalyticsJourneyAudienceFilters, UnsetType] = unset,
        graph_filters: Union[List[ProductAnalyticsJourneySearchGraphFilter], UnsetType] = unset,
        string_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Filters applied on top of the journey step expression.

        :param audience_filters: Restricts the journey to an audience built from named sub-queries.
            Sub-query names must be unique across ``users`` , ``segments`` , and ``accounts``.
        :type audience_filters: ProductAnalyticsJourneyAudienceFilters, optional

        :param graph_filters: Filters on journey-level metrics such as time to convert.
        :type graph_filters: [ProductAnalyticsJourneySearchGraphFilter], optional

        :param string_filter: Free-text search query applied to the whole journey.
        :type string_filter: str, optional
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if graph_filters is not unset:
            kwargs["graph_filters"] = graph_filters
        if string_filter is not unset:
            kwargs["string_filter"] = string_filter
        super().__init__(kwargs)
