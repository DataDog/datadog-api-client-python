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
    from datadog_api_client.v2.model.product_analytics_journey_funnel_compute import (
        ProductAnalyticsJourneyFunnelCompute,
    )
    from datadog_api_client.v2.model.product_analytics_graph_query_group_by import ProductAnalyticsGraphQueryGroupBy
    from datadog_api_client.v2.model.product_analytics_journey_search import ProductAnalyticsJourneySearch


class ProductAnalyticsJourneyFunnelQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_funnel_compute import (
            ProductAnalyticsJourneyFunnelCompute,
        )
        from datadog_api_client.v2.model.product_analytics_graph_query_group_by import ProductAnalyticsGraphQueryGroupBy
        from datadog_api_client.v2.model.product_analytics_journey_search import ProductAnalyticsJourneySearch

        return {
            "compute": (ProductAnalyticsJourneyFunnelCompute,),
            "group_by": ([ProductAnalyticsGraphQueryGroupBy],),
            "search": (ProductAnalyticsJourneySearch,),
        }

    attribute_map = {
        "compute": "compute",
        "group_by": "group_by",
        "search": "search",
    }

    def __init__(
        self_,
        search: ProductAnalyticsJourneySearch,
        compute: Union[ProductAnalyticsJourneyFunnelCompute, UnsetType] = unset,
        group_by: Union[List[ProductAnalyticsGraphQueryGroupBy], UnsetType] = unset,
        **kwargs,
    ):
        """
        Query definition for a journey funnel request.

        :param compute: Defines the metric computed at each funnel step.
        :type compute: ProductAnalyticsJourneyFunnelCompute, optional

        :param group_by: Segments the funnel by the values of one or more facets.
        :type group_by: [ProductAnalyticsGraphQueryGroupBy], optional

        :param search: Defines the steps of the journey and the filters applied to it.
        :type search: ProductAnalyticsJourneySearch
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_.search = search
