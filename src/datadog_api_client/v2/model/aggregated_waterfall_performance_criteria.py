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
    from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria_metric import (
        AggregatedWaterfallPerformanceCriteriaMetric,
    )


class AggregatedWaterfallPerformanceCriteria(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria_metric import (
            AggregatedWaterfallPerformanceCriteriaMetric,
        )

        return {
            "max": (float,),
            "metric": (AggregatedWaterfallPerformanceCriteriaMetric,),
            "min": (float,),
        }

    attribute_map = {
        "max": "max",
        "metric": "metric",
        "min": "min",
    }

    def __init__(
        self_,
        metric: AggregatedWaterfallPerformanceCriteriaMetric,
        max: Union[float, UnsetType] = unset,
        min: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Performance criteria to filter view instances by a metric threshold.

        :param max: Maximum threshold in seconds (inclusive).
        :type max: float, optional

        :param metric: Performance metric used to filter view instances by threshold.
        :type metric: AggregatedWaterfallPerformanceCriteriaMetric

        :param min: Minimum threshold in seconds (inclusive).
        :type min: float, optional
        """
        if max is not unset:
            kwargs["max"] = max
        if min is not unset:
            kwargs["min"] = min
        super().__init__(kwargs)

        self_.metric = metric
