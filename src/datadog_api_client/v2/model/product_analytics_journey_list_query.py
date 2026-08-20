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
    from datadog_api_client.v2.model.product_analytics_journey_computed_column import (
        ProductAnalyticsJourneyComputedColumn,
    )
    from datadog_api_client.v2.model.product_analytics_journey_conversion_type import (
        ProductAnalyticsJourneyConversionType,
    )
    from datadog_api_client.v2.model.product_analytics_graph_query_group_by import ProductAnalyticsGraphQueryGroupBy
    from datadog_api_client.v2.model.product_analytics_journey_search import ProductAnalyticsJourneySearch
    from datadog_api_client.v2.model.product_analytics_journey_list_sort import ProductAnalyticsJourneyListSort
    from datadog_api_client.v2.model.product_analytics_journey_target import ProductAnalyticsJourneyTarget
    from datadog_api_client.v2.model.product_analytics_journey_node_target import ProductAnalyticsJourneyNodeTarget
    from datadog_api_client.v2.model.product_analytics_journey_path_target import ProductAnalyticsJourneyPathTarget


class ProductAnalyticsJourneyListQuery(ModelNormal):
    validations = {
        "limit": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_computed_column import (
            ProductAnalyticsJourneyComputedColumn,
        )
        from datadog_api_client.v2.model.product_analytics_journey_conversion_type import (
            ProductAnalyticsJourneyConversionType,
        )
        from datadog_api_client.v2.model.product_analytics_graph_query_group_by import ProductAnalyticsGraphQueryGroupBy
        from datadog_api_client.v2.model.product_analytics_journey_search import ProductAnalyticsJourneySearch
        from datadog_api_client.v2.model.product_analytics_journey_list_sort import ProductAnalyticsJourneyListSort
        from datadog_api_client.v2.model.product_analytics_journey_target import ProductAnalyticsJourneyTarget

        return {
            "computed_columns": ([ProductAnalyticsJourneyComputedColumn],),
            "conversion_type": (ProductAnalyticsJourneyConversionType,),
            "entity_columns": ([str],),
            "entity_filters": (str,),
            "group_by": ([ProductAnalyticsGraphQueryGroupBy],),
            "limit": (int,),
            "search": (ProductAnalyticsJourneySearch,),
            "sort": (ProductAnalyticsJourneyListSort,),
            "target": (ProductAnalyticsJourneyTarget,),
        }

    attribute_map = {
        "computed_columns": "computed_columns",
        "conversion_type": "conversion_type",
        "entity_columns": "entity_columns",
        "entity_filters": "entity_filters",
        "group_by": "group_by",
        "limit": "limit",
        "search": "search",
        "sort": "sort",
        "target": "target",
    }

    def __init__(
        self_,
        search: ProductAnalyticsJourneySearch,
        computed_columns: Union[List[ProductAnalyticsJourneyComputedColumn], UnsetType] = unset,
        conversion_type: Union[ProductAnalyticsJourneyConversionType, UnsetType] = unset,
        entity_columns: Union[List[str], UnsetType] = unset,
        entity_filters: Union[str, UnsetType] = unset,
        group_by: Union[List[ProductAnalyticsGraphQueryGroupBy], UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        sort: Union[ProductAnalyticsJourneyListSort, UnsetType] = unset,
        target: Union[
            ProductAnalyticsJourneyTarget,
            ProductAnalyticsJourneyNodeTarget,
            ProductAnalyticsJourneyPathTarget,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Query definition for a journey list request.

        :param computed_columns: Computed columns to add to each row.
        :type computed_columns: [ProductAnalyticsJourneyComputedColumn], optional

        :param conversion_type: Whether to return the entities that converted at the target step, or those that dropped off.
        :type conversion_type: ProductAnalyticsJourneyConversionType, optional

        :param entity_columns: Attribute columns to return for each row, in addition to the identity join key and ``timestamp``.
        :type entity_columns: [str], optional

        :param entity_filters: Additional search query applied to the returned rows.
        :type entity_filters: str, optional

        :param group_by: Segments the results by the values of one or more facets.
        :type group_by: [ProductAnalyticsGraphQueryGroupBy], optional

        :param limit: Maximum number of rows to return. Omit it to let the service choose.
        :type limit: int, optional

        :param search: Defines the steps of the journey and the filters applied to it.
        :type search: ProductAnalyticsJourneySearch

        :param sort: Sort configuration for the returned rows. The sort is applied only when ``facet``
            is one of the returned columns; otherwise it is ignored.
        :type sort: ProductAnalyticsJourneyListSort, optional

        :param target: A reference to a step, or a range of steps, in the journey.
            Use a ``node`` target to name a single step, or a ``path`` target to name the range
            between two steps.
        :type target: ProductAnalyticsJourneyTarget, optional
        """
        if computed_columns is not unset:
            kwargs["computed_columns"] = computed_columns
        if conversion_type is not unset:
            kwargs["conversion_type"] = conversion_type
        if entity_columns is not unset:
            kwargs["entity_columns"] = entity_columns
        if entity_filters is not unset:
            kwargs["entity_filters"] = entity_filters
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if limit is not unset:
            kwargs["limit"] = limit
        if sort is not unset:
            kwargs["sort"] = sort
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.search = search
