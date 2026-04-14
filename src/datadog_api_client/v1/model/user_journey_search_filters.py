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
    from datadog_api_client.v1.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
    from datadog_api_client.v1.model.user_journey_search_graph_filter import UserJourneySearchGraphFilter


class UserJourneySearchFilters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
        from datadog_api_client.v1.model.user_journey_search_graph_filter import UserJourneySearchGraphFilter

        return {
            "audience_filters": (ProductAnalyticsAudienceFilters,),
            "graph_filters": ([UserJourneySearchGraphFilter],),
            "string_filter": (str,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "graph_filters": "graph_filters",
        "string_filter": "string_filter",
    }

    def __init__(
        self_,
        audience_filters: Union[ProductAnalyticsAudienceFilters, UnsetType] = unset,
        graph_filters: Union[List[UserJourneySearchGraphFilter], UnsetType] = unset,
        string_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Filters for user journey search.

        :param audience_filters: Product Analytics/RUM audience filters.
        :type audience_filters: ProductAnalyticsAudienceFilters, optional

        :param graph_filters: Graph filters.
        :type graph_filters: [UserJourneySearchGraphFilter], optional

        :param string_filter: String filter.
        :type string_filter: str, optional
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if graph_filters is not unset:
            kwargs["graph_filters"] = graph_filters
        if string_filter is not unset:
            kwargs["string_filter"] = string_filter
        super().__init__(kwargs)
