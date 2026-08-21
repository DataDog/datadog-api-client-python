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


class ProductAnalyticsJourneyFunnelStepGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_elapsed_time import ProductAnalyticsElapsedTime

        return {
            "conversion_count": (int,),
            "elapsed_time_to_next_step": (ProductAnalyticsElapsedTime,),
            "group_tags": ([str],),
            "value": (float,),
        }

    attribute_map = {
        "conversion_count": "conversion_count",
        "elapsed_time_to_next_step": "elapsed_time_to_next_step",
        "group_tags": "group_tags",
        "value": "value",
    }

    def __init__(
        self_,
        conversion_count: int,
        elapsed_time_to_next_step: ProductAnalyticsElapsedTime,
        group_tags: List[str],
        value: float,
        **kwargs,
    ):
        """
        Breakdown of a funnel step for one combination of group-by values.

        :param conversion_count: Number of entities in this group that reached the next step.
        :type conversion_count: int

        :param elapsed_time_to_next_step: Elapsed time statistics (min/max/avg in milliseconds).
        :type elapsed_time_to_next_step: ProductAnalyticsElapsedTime

        :param group_tags: Group-by values identifying this cohort.
        :type group_tags: [str]

        :param value: Value of the computed metric for this group at this step.
        :type value: float
        """
        super().__init__(kwargs)

        self_.conversion_count = conversion_count
        self_.elapsed_time_to_next_step = elapsed_time_to_next_step
        self_.group_tags = group_tags
        self_.value = value
