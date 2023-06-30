# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SpansAggregationFunction(ModelSimple):
    """
    An aggregation function.

    :param value: Must be one of ["count", "cardinality", "pc75", "pc90", "pc95", "pc98", "pc99", "sum", "min", "max", "avg", "median"].
    :type value: str
    """

    allowed_values = {
        "count",
        "cardinality",
        "pc75",
        "pc90",
        "pc95",
        "pc98",
        "pc99",
        "sum",
        "min",
        "max",
        "avg",
        "median",
    }
    COUNT: ClassVar["SpansAggregationFunction"]
    CARDINALITY: ClassVar["SpansAggregationFunction"]
    PERCENTILE_75: ClassVar["SpansAggregationFunction"]
    PERCENTILE_90: ClassVar["SpansAggregationFunction"]
    PERCENTILE_95: ClassVar["SpansAggregationFunction"]
    PERCENTILE_98: ClassVar["SpansAggregationFunction"]
    PERCENTILE_99: ClassVar["SpansAggregationFunction"]
    SUM: ClassVar["SpansAggregationFunction"]
    MIN: ClassVar["SpansAggregationFunction"]
    MAX: ClassVar["SpansAggregationFunction"]
    AVG: ClassVar["SpansAggregationFunction"]
    MEDIAN: ClassVar["SpansAggregationFunction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SpansAggregationFunction.COUNT = SpansAggregationFunction("count")
SpansAggregationFunction.CARDINALITY = SpansAggregationFunction("cardinality")
SpansAggregationFunction.PERCENTILE_75 = SpansAggregationFunction("pc75")
SpansAggregationFunction.PERCENTILE_90 = SpansAggregationFunction("pc90")
SpansAggregationFunction.PERCENTILE_95 = SpansAggregationFunction("pc95")
SpansAggregationFunction.PERCENTILE_98 = SpansAggregationFunction("pc98")
SpansAggregationFunction.PERCENTILE_99 = SpansAggregationFunction("pc99")
SpansAggregationFunction.SUM = SpansAggregationFunction("sum")
SpansAggregationFunction.MIN = SpansAggregationFunction("min")
SpansAggregationFunction.MAX = SpansAggregationFunction("max")
SpansAggregationFunction.AVG = SpansAggregationFunction("avg")
SpansAggregationFunction.MEDIAN = SpansAggregationFunction("median")
