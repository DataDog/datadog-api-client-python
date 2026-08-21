# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricEstimateType(ModelSimple):
    """
    Estimate type based on the queried configuration. `count_or_gauge` is returned by default, and `distribution` is returned for distribution metrics. The `filter[pct]` query parameter has no effect on this value.

    :param value: If omitted defaults to "count_or_gauge". Must be one of ["count_or_gauge", "distribution", "percentile"].
    :type value: str
    """

    allowed_values = {
        "count_or_gauge",
        "distribution",
        "percentile",
    }
    COUNT_OR_GAUGE: ClassVar["MetricEstimateType"]
    DISTRIBUTION: ClassVar["MetricEstimateType"]
    PERCENTILE: ClassVar["MetricEstimateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricEstimateType.COUNT_OR_GAUGE = MetricEstimateType("count_or_gauge")
MetricEstimateType.DISTRIBUTION = MetricEstimateType("distribution")
MetricEstimateType.PERCENTILE = MetricEstimateType("percentile")
