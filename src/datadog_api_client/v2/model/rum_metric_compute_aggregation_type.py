# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumMetricComputeAggregationType(ModelSimple):
    """
    The type of aggregation to use.

    :param value: Must be one of ["count", "distribution"].
    :type value: str
    """

    allowed_values = {
        "count",
        "distribution",
    }
    COUNT: ClassVar["RumMetricComputeAggregationType"]
    DISTRIBUTION: ClassVar["RumMetricComputeAggregationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumMetricComputeAggregationType.COUNT = RumMetricComputeAggregationType("count")
RumMetricComputeAggregationType.DISTRIBUTION = RumMetricComputeAggregationType("distribution")
