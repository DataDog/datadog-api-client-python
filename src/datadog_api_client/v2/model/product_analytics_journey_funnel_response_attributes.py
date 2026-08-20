# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_elapsed_time import ProductAnalyticsElapsedTime
    from datadog_api_client.v2.model.product_analytics_journey_funnel_step import ProductAnalyticsJourneyFunnelStep


class ProductAnalyticsJourneyFunnelResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_elapsed_time import ProductAnalyticsElapsedTime
        from datadog_api_client.v2.model.product_analytics_journey_funnel_step import ProductAnalyticsJourneyFunnelStep

        return {
            "end_to_end_conversion_rate": (float,),
            "end_to_end_elapsed_time": (ProductAnalyticsElapsedTime,),
            "funnel_steps": ([ProductAnalyticsJourneyFunnelStep],),
            "initial_count": (int,),
        }

    attribute_map = {
        "end_to_end_conversion_rate": "end_to_end_conversion_rate",
        "end_to_end_elapsed_time": "end_to_end_elapsed_time",
        "funnel_steps": "funnel_steps",
        "initial_count": "initial_count",
    }

    def __init__(
        self_,
        end_to_end_conversion_rate: float,
        end_to_end_elapsed_time: ProductAnalyticsElapsedTime,
        funnel_steps: List[ProductAnalyticsJourneyFunnelStep],
        initial_count: int,
        **kwargs,
    ):
        """
        Attributes of a journey funnel response.

        :param end_to_end_conversion_rate: Conversion rate from the first step to the last step.
        :type end_to_end_conversion_rate: float

        :param end_to_end_elapsed_time: Elapsed time statistics (min/max/avg in milliseconds).
        :type end_to_end_elapsed_time: ProductAnalyticsElapsedTime

        :param funnel_steps: The funnel steps, in the order given by the search expression.
        :type funnel_steps: [ProductAnalyticsJourneyFunnelStep]

        :param initial_count: Number of entities that entered the funnel.
        :type initial_count: int
        """
        super().__init__(kwargs)

        self_.end_to_end_conversion_rate = end_to_end_conversion_rate
        self_.end_to_end_elapsed_time = end_to_end_elapsed_time
        self_.funnel_steps = funnel_steps
        self_.initial_count = initial_count
