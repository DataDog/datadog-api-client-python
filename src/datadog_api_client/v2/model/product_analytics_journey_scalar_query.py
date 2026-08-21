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
    from datadog_api_client.v2.model.product_analytics_journey_scalar_compute import (
        ProductAnalyticsJourneyScalarCompute,
    )
    from datadog_api_client.v2.model.product_analytics_graph_query_group_by import ProductAnalyticsGraphQueryGroupBy
    from datadog_api_client.v2.model.product_analytics_journey_search import ProductAnalyticsJourneySearch


class ProductAnalyticsJourneyScalarQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_scalar_compute import (
            ProductAnalyticsJourneyScalarCompute,
        )
        from datadog_api_client.v2.model.product_analytics_graph_query_group_by import ProductAnalyticsGraphQueryGroupBy
        from datadog_api_client.v2.model.product_analytics_journey_search import ProductAnalyticsJourneySearch

        return {
            "compute": (ProductAnalyticsJourneyScalarCompute,),
            "group_by": ([ProductAnalyticsGraphQueryGroupBy],),
            "query_id": (str,),
            "search": (ProductAnalyticsJourneySearch,),
        }

    attribute_map = {
        "compute": "compute",
        "group_by": "group_by",
        "query_id": "query_id",
        "search": "search",
    }

    def __init__(
        self_,
        compute: ProductAnalyticsJourneyScalarCompute,
        search: ProductAnalyticsJourneySearch,
        group_by: Union[List[ProductAnalyticsGraphQueryGroupBy], UnsetType] = unset,
        query_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query definition for a journey scalar request.

        :param compute: Defines the metric computed over the journey for a scalar query.
        :type compute: ProductAnalyticsJourneyScalarCompute

        :param group_by: Segments the results by the values of one or more facets.
        :type group_by: [ProductAnalyticsGraphQueryGroupBy], optional

        :param query_id: Caller-defined identifier echoed back in the results.
        :type query_id: str, optional

        :param search: Defines the steps of the journey and the filters applied to it.
        :type search: ProductAnalyticsJourneySearch
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if query_id is not unset:
            kwargs["query_id"] = query_id
        super().__init__(kwargs)

        self_.compute = compute
        self_.search = search
