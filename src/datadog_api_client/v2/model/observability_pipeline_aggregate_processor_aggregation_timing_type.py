# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAggregateProcessorAggregationTimingType(ModelSimple):
    """
    Determines whether metrics are assigned to aggregation windows based on when they are processed or their timestamps.

    :param value: Must be one of ["system_time", "event_time"].
    :type value: str
    """

    allowed_values = {
        "system_time",
        "event_time",
    }
    SYSTEM_TIME: ClassVar["ObservabilityPipelineAggregateProcessorAggregationTimingType"]
    EVENT_TIME: ClassVar["ObservabilityPipelineAggregateProcessorAggregationTimingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAggregateProcessorAggregationTimingType.SYSTEM_TIME = (
    ObservabilityPipelineAggregateProcessorAggregationTimingType("system_time")
)
ObservabilityPipelineAggregateProcessorAggregationTimingType.EVENT_TIME = (
    ObservabilityPipelineAggregateProcessorAggregationTimingType("event_time")
)
