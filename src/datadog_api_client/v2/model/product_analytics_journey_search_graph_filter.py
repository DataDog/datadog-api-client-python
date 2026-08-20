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
    from datadog_api_client.v2.model.product_analytics_journey_search_graph_filter_name import (
        ProductAnalyticsJourneySearchGraphFilterName,
    )
    from datadog_api_client.v2.model.product_analytics_journey_search_graph_filter_operator import (
        ProductAnalyticsJourneySearchGraphFilterOperator,
    )
    from datadog_api_client.v2.model.product_analytics_journey_target import ProductAnalyticsJourneyTarget
    from datadog_api_client.v2.model.product_analytics_journey_node_target import ProductAnalyticsJourneyNodeTarget
    from datadog_api_client.v2.model.product_analytics_journey_path_target import ProductAnalyticsJourneyPathTarget


class ProductAnalyticsJourneySearchGraphFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_search_graph_filter_name import (
            ProductAnalyticsJourneySearchGraphFilterName,
        )
        from datadog_api_client.v2.model.product_analytics_journey_search_graph_filter_operator import (
            ProductAnalyticsJourneySearchGraphFilterOperator,
        )
        from datadog_api_client.v2.model.product_analytics_journey_target import ProductAnalyticsJourneyTarget

        return {
            "name": (ProductAnalyticsJourneySearchGraphFilterName,),
            "operator": (ProductAnalyticsJourneySearchGraphFilterOperator,),
            "target": (ProductAnalyticsJourneyTarget,),
            "value": (int,),
        }

    attribute_map = {
        "name": "name",
        "operator": "operator",
        "target": "target",
        "value": "value",
    }

    def __init__(
        self_,
        name: ProductAnalyticsJourneySearchGraphFilterName,
        operator: ProductAnalyticsJourneySearchGraphFilterOperator,
        value: int,
        target: Union[
            ProductAnalyticsJourneyTarget,
            ProductAnalyticsJourneyNodeTarget,
            ProductAnalyticsJourneyPathTarget,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        A filter applied to a step, or a range of steps, of the journey graph.

        :param name: The journey-level metric the graph filter applies to.
        :type name: ProductAnalyticsJourneySearchGraphFilterName

        :param operator: Comparison operator applied to the graph filter value.
        :type operator: ProductAnalyticsJourneySearchGraphFilterOperator

        :param target: A reference to a step, or a range of steps, in the journey.
            Use a ``node`` target to name a single step, or a ``path`` target to name the range
            between two steps.
        :type target: ProductAnalyticsJourneyTarget, optional

        :param value: Value compared against the metric. Durations are expressed in milliseconds.
        :type value: int
        """
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.name = name
        self_.operator = operator
        self_.value = value
