# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineGeneratedMetricMetricType(ModelSimple):
    """
    Type of metric to create.

    :param value: Must be one of ["count", "gauge", "distribution"].
    :type value: str
    """

    allowed_values = {
        "count",
        "gauge",
        "distribution",
    }
    COUNT: ClassVar["ObservabilityPipelineGeneratedMetricMetricType"]
    GAUGE: ClassVar["ObservabilityPipelineGeneratedMetricMetricType"]
    DISTRIBUTION: ClassVar["ObservabilityPipelineGeneratedMetricMetricType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineGeneratedMetricMetricType.COUNT = ObservabilityPipelineGeneratedMetricMetricType("count")
ObservabilityPipelineGeneratedMetricMetricType.GAUGE = ObservabilityPipelineGeneratedMetricMetricType("gauge")
ObservabilityPipelineGeneratedMetricMetricType.DISTRIBUTION = ObservabilityPipelineGeneratedMetricMetricType(
    "distribution"
)
