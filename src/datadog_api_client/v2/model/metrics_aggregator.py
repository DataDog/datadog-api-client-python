# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricsAggregator(ModelSimple):
    """
    The type of aggregation that can be performed on metrics queries.

    :param value: If omitted defaults to "avg". Must be one of ["avg", "min", "max", "sum", "last"].
    :type value: str
    """

    allowed_values = {
        "avg",
        "min",
        "max",
        "sum",
        "last",
    }
    AVG: ClassVar["MetricsAggregator"]
    MIN: ClassVar["MetricsAggregator"]
    MAX: ClassVar["MetricsAggregator"]
    SUM: ClassVar["MetricsAggregator"]
    LAST: ClassVar["MetricsAggregator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricsAggregator.AVG = MetricsAggregator("avg")
MetricsAggregator.MIN = MetricsAggregator("min")
MetricsAggregator.MAX = MetricsAggregator("max")
MetricsAggregator.SUM = MetricsAggregator("sum")
MetricsAggregator.LAST = MetricsAggregator("last")
