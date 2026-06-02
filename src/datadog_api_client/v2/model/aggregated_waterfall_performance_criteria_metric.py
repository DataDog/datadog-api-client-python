# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AggregatedWaterfallPerformanceCriteriaMetric(ModelSimple):
    """
    Performance metric used to filter view instances by threshold.

    :param value: Must be one of ["loading_time", "largest_contentful_paint", "first_contentful_paint", "interaction_to_next_paint"].
    :type value: str
    """

    allowed_values = {
        "loading_time",
        "largest_contentful_paint",
        "first_contentful_paint",
        "interaction_to_next_paint",
    }
    LOADING_TIME: ClassVar["AggregatedWaterfallPerformanceCriteriaMetric"]
    LARGEST_CONTENTFUL_PAINT: ClassVar["AggregatedWaterfallPerformanceCriteriaMetric"]
    FIRST_CONTENTFUL_PAINT: ClassVar["AggregatedWaterfallPerformanceCriteriaMetric"]
    INTERACTION_TO_NEXT_PAINT: ClassVar["AggregatedWaterfallPerformanceCriteriaMetric"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AggregatedWaterfallPerformanceCriteriaMetric.LOADING_TIME = AggregatedWaterfallPerformanceCriteriaMetric("loading_time")
AggregatedWaterfallPerformanceCriteriaMetric.LARGEST_CONTENTFUL_PAINT = AggregatedWaterfallPerformanceCriteriaMetric(
    "largest_contentful_paint"
)
AggregatedWaterfallPerformanceCriteriaMetric.FIRST_CONTENTFUL_PAINT = AggregatedWaterfallPerformanceCriteriaMetric(
    "first_contentful_paint"
)
AggregatedWaterfallPerformanceCriteriaMetric.INTERACTION_TO_NEXT_PAINT = AggregatedWaterfallPerformanceCriteriaMetric(
    "interaction_to_next_paint"
)
