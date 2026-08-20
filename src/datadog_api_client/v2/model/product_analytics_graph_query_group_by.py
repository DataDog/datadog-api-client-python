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
    from datadog_api_client.v2.model.product_analytics_group_by_sort import ProductAnalyticsGroupBySort
    from datadog_api_client.v2.model.product_analytics_graph_query_group_by_source import (
        ProductAnalyticsGraphQueryGroupBySource,
    )
    from datadog_api_client.v2.model.product_analytics_journey_target import ProductAnalyticsJourneyTarget
    from datadog_api_client.v2.model.product_analytics_journey_node_target import ProductAnalyticsJourneyNodeTarget
    from datadog_api_client.v2.model.product_analytics_journey_path_target import ProductAnalyticsJourneyPathTarget


class ProductAnalyticsGraphQueryGroupBy(ModelNormal):
    validations = {
        "limit": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_group_by_sort import ProductAnalyticsGroupBySort
        from datadog_api_client.v2.model.product_analytics_graph_query_group_by_source import (
            ProductAnalyticsGraphQueryGroupBySource,
        )
        from datadog_api_client.v2.model.product_analytics_journey_target import ProductAnalyticsJourneyTarget

        return {
            "facet": (str,),
            "limit": (int,),
            "should_exclude_missing": (bool,),
            "sort": (ProductAnalyticsGroupBySort,),
            "source": (ProductAnalyticsGraphQueryGroupBySource,),
            "target": (ProductAnalyticsJourneyTarget,),
            "value_filters": ([str],),
        }

    attribute_map = {
        "facet": "facet",
        "limit": "limit",
        "should_exclude_missing": "should_exclude_missing",
        "sort": "sort",
        "source": "source",
        "target": "target",
        "value_filters": "value_filters",
    }

    def __init__(
        self_,
        facet: str,
        limit: Union[int, UnsetType] = unset,
        should_exclude_missing: Union[bool, UnsetType] = unset,
        sort: Union[ProductAnalyticsGroupBySort, UnsetType] = unset,
        source: Union[ProductAnalyticsGraphQueryGroupBySource, UnsetType] = unset,
        target: Union[
            ProductAnalyticsJourneyTarget,
            ProductAnalyticsJourneyNodeTarget,
            ProductAnalyticsJourneyPathTarget,
            UnsetType,
        ] = unset,
        value_filters: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Segments journey results by the values of a facet.

        :param facet: Attribute path to group by.
        :type facet: str

        :param limit: Maximum number of groups to return. Omit it to let the service choose.
        :type limit: int, optional

        :param should_exclude_missing: Whether to exclude entities that have no value for this facet.
        :type should_exclude_missing: bool, optional

        :param sort: Sort configuration for group-by results.
        :type sort: ProductAnalyticsGroupBySort, optional

        :param source: Audience dimension to group by, instead of an event facet.
        :type source: ProductAnalyticsGraphQueryGroupBySource, optional

        :param target: A reference to a step, or a range of steps, in the journey.
            Use a ``node`` target to name a single step, or a ``path`` target to name the range
            between two steps.
        :type target: ProductAnalyticsJourneyTarget, optional

        :param value_filters: Restricts the results to these facet values.
        :type value_filters: [str], optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if should_exclude_missing is not unset:
            kwargs["should_exclude_missing"] = should_exclude_missing
        if sort is not unset:
            kwargs["sort"] = sort
        if source is not unset:
            kwargs["source"] = source
        if target is not unset:
            kwargs["target"] = target
        if value_filters is not unset:
            kwargs["value_filters"] = value_filters
        super().__init__(kwargs)

        self_.facet = facet
