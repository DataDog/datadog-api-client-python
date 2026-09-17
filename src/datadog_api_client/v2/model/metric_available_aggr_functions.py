# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricAvailableAggrFunctions(ModelSimple):
    """
    A single aggregation function used to query a metric.

    :param value: Must be one of ["avg", "min", "max", "sum", "count", "stddev", "pxx"].
    :type value: str
    """

    allowed_values = {
        "avg",
        "min",
        "max",
        "sum",
        "count",
        "stddev",
        "pxx",
    }
    AVG: ClassVar["MetricAvailableAggrFunctions"]
    MIN: ClassVar["MetricAvailableAggrFunctions"]
    MAX: ClassVar["MetricAvailableAggrFunctions"]
    SUM: ClassVar["MetricAvailableAggrFunctions"]
    COUNT: ClassVar["MetricAvailableAggrFunctions"]
    STDDEV: ClassVar["MetricAvailableAggrFunctions"]
    PXX: ClassVar["MetricAvailableAggrFunctions"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricAvailableAggrFunctions.AVG = MetricAvailableAggrFunctions("avg")
MetricAvailableAggrFunctions.MIN = MetricAvailableAggrFunctions("min")
MetricAvailableAggrFunctions.MAX = MetricAvailableAggrFunctions("max")
MetricAvailableAggrFunctions.SUM = MetricAvailableAggrFunctions("sum")
MetricAvailableAggrFunctions.COUNT = MetricAvailableAggrFunctions("count")
MetricAvailableAggrFunctions.STDDEV = MetricAvailableAggrFunctions("stddev")
MetricAvailableAggrFunctions.PXX = MetricAvailableAggrFunctions("pxx")
