# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAggregateProcessorMode(ModelSimple):
    """
    The aggregation mode applied to metrics that share the same name and tags within the interval.

    :param value: Must be one of ["auto", "sum", "latest", "count", "max", "min", "mean"].
    :type value: str
    """

    allowed_values = {
        "auto",
        "sum",
        "latest",
        "count",
        "max",
        "min",
        "mean",
    }
    AUTO: ClassVar["ObservabilityPipelineAggregateProcessorMode"]
    SUM: ClassVar["ObservabilityPipelineAggregateProcessorMode"]
    LATEST: ClassVar["ObservabilityPipelineAggregateProcessorMode"]
    COUNT: ClassVar["ObservabilityPipelineAggregateProcessorMode"]
    MAX: ClassVar["ObservabilityPipelineAggregateProcessorMode"]
    MIN: ClassVar["ObservabilityPipelineAggregateProcessorMode"]
    MEAN: ClassVar["ObservabilityPipelineAggregateProcessorMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAggregateProcessorMode.AUTO = ObservabilityPipelineAggregateProcessorMode("auto")
ObservabilityPipelineAggregateProcessorMode.SUM = ObservabilityPipelineAggregateProcessorMode("sum")
ObservabilityPipelineAggregateProcessorMode.LATEST = ObservabilityPipelineAggregateProcessorMode("latest")
ObservabilityPipelineAggregateProcessorMode.COUNT = ObservabilityPipelineAggregateProcessorMode("count")
ObservabilityPipelineAggregateProcessorMode.MAX = ObservabilityPipelineAggregateProcessorMode("max")
ObservabilityPipelineAggregateProcessorMode.MIN = ObservabilityPipelineAggregateProcessorMode("min")
ObservabilityPipelineAggregateProcessorMode.MEAN = ObservabilityPipelineAggregateProcessorMode("mean")
