# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_journey_search_filters import (
        ProductAnalyticsJourneySearchFilters,
    )
    from datadog_api_client.v2.model.product_analytics_join_keys import ProductAnalyticsJoinKeys
    from datadog_api_client.v2.model.product_analytics_base_query import ProductAnalyticsBaseQuery
    from datadog_api_client.v2.model.product_analytics_event_query import ProductAnalyticsEventQuery
    from datadog_api_client.v2.model.product_analytics_occurrence_query import ProductAnalyticsOccurrenceQuery


class ProductAnalyticsJourneySearch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_search_filters import (
            ProductAnalyticsJourneySearchFilters,
        )
        from datadog_api_client.v2.model.product_analytics_join_keys import ProductAnalyticsJoinKeys
        from datadog_api_client.v2.model.product_analytics_base_query import ProductAnalyticsBaseQuery

        return {
            "expression": (str,),
            "filters": (ProductAnalyticsJourneySearchFilters,),
            "join_keys": (ProductAnalyticsJoinKeys,),
            "node_objects": ({str: (ProductAnalyticsBaseQuery,)},),
        }

    attribute_map = {
        "expression": "expression",
        "filters": "filters",
        "join_keys": "join_keys",
        "node_objects": "node_objects",
    }

    def __init__(
        self_,
        expression: str,
        node_objects: Dict[
            str, Union[ProductAnalyticsBaseQuery, ProductAnalyticsEventQuery, ProductAnalyticsOccurrenceQuery]
        ],
        filters: Union[ProductAnalyticsJourneySearchFilters, UnsetType] = unset,
        join_keys: Union[ProductAnalyticsJoinKeys, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines the steps of the journey and the filters applied to it.

        :param expression: Expression combining the node aliases in order, for example ``A -> B -> C``.
        :type expression: str

        :param filters: Filters applied on top of the journey step expression.
        :type filters: ProductAnalyticsJourneySearchFilters, optional

        :param join_keys: Identity join keys used to stitch events belonging to the same user or session.
        :type join_keys: ProductAnalyticsJoinKeys, optional

        :param node_objects: Map of node alias to the query matching that step of the journey.
            Every alias used in ``expression`` must have an entry here.
        :type node_objects: {str: (ProductAnalyticsBaseQuery,)}
        """
        if filters is not unset:
            kwargs["filters"] = filters
        if join_keys is not unset:
            kwargs["join_keys"] = join_keys
        super().__init__(kwargs)

        self_.expression = expression
        self_.node_objects = node_objects
