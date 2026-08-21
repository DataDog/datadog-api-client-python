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
    from datadog_api_client.v2.model.product_analytics_journey_funnel_step_group import (
        ProductAnalyticsJourneyFunnelStepGroup,
    )


class ProductAnalyticsJourneyFunnelStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_elapsed_time import ProductAnalyticsElapsedTime
        from datadog_api_client.v2.model.product_analytics_journey_funnel_step_group import (
            ProductAnalyticsJourneyFunnelStepGroup,
        )

        return {
            "elapsed_time_to_next_step": (ProductAnalyticsElapsedTime,),
            "groups": ([ProductAnalyticsJourneyFunnelStepGroup],),
            "label": (str,),
            "unit": (str,),
            "value": (float,),
        }

    attribute_map = {
        "elapsed_time_to_next_step": "elapsed_time_to_next_step",
        "groups": "groups",
        "label": "label",
        "unit": "unit",
        "value": "value",
    }

    def __init__(
        self_,
        elapsed_time_to_next_step: ProductAnalyticsElapsedTime,
        groups: List[ProductAnalyticsJourneyFunnelStepGroup],
        label: str,
        unit: str,
        value: float,
        **kwargs,
    ):
        """
        A single step of the funnel with its conversion counts and timings.

        :param elapsed_time_to_next_step: Elapsed time statistics (min/max/avg in milliseconds).
        :type elapsed_time_to_next_step: ProductAnalyticsElapsedTime

        :param groups: Breakdown of this step by the requested group-by facets.
        :type groups: [ProductAnalyticsJourneyFunnelStepGroup]

        :param label: Label of the step, derived from the node alias.
        :type label: str

        :param unit: Unit of the elapsed time values.
        :type unit: str

        :param value: Value of the computed metric at this step.
        :type value: float
        """
        super().__init__(kwargs)

        self_.elapsed_time_to_next_step = elapsed_time_to_next_step
        self_.groups = groups
        self_.label = label
        self_.unit = unit
        self_.value = value
