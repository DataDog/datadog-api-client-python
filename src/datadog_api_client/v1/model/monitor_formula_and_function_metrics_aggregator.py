# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionMetricsAggregator(ModelSimple):
    """
    Aggregator for metrics queries.

    :param value: Must be one of ["avg", "min", "max", "sum", "last", "mean", "area", "l2norm", "percentile", "stddev", "count_unique"].
    :type value: str
    """

    allowed_values = {
        "avg",
        "min",
        "max",
        "sum",
        "last",
        "mean",
        "area",
        "l2norm",
        "percentile",
        "stddev",
        "count_unique",
    }
    AVG: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]
    MIN: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]
    MAX: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]
    SUM: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]
    LAST: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]
    MEAN: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]
    AREA: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]
    L2NORM: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]
    PERCENTILE: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]
    STDDEV: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]
    COUNT_UNIQUE: ClassVar["MonitorFormulaAndFunctionMetricsAggregator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionMetricsAggregator.AVG = MonitorFormulaAndFunctionMetricsAggregator("avg")
MonitorFormulaAndFunctionMetricsAggregator.MIN = MonitorFormulaAndFunctionMetricsAggregator("min")
MonitorFormulaAndFunctionMetricsAggregator.MAX = MonitorFormulaAndFunctionMetricsAggregator("max")
MonitorFormulaAndFunctionMetricsAggregator.SUM = MonitorFormulaAndFunctionMetricsAggregator("sum")
MonitorFormulaAndFunctionMetricsAggregator.LAST = MonitorFormulaAndFunctionMetricsAggregator("last")
MonitorFormulaAndFunctionMetricsAggregator.MEAN = MonitorFormulaAndFunctionMetricsAggregator("mean")
MonitorFormulaAndFunctionMetricsAggregator.AREA = MonitorFormulaAndFunctionMetricsAggregator("area")
MonitorFormulaAndFunctionMetricsAggregator.L2NORM = MonitorFormulaAndFunctionMetricsAggregator("l2norm")
MonitorFormulaAndFunctionMetricsAggregator.PERCENTILE = MonitorFormulaAndFunctionMetricsAggregator("percentile")
MonitorFormulaAndFunctionMetricsAggregator.STDDEV = MonitorFormulaAndFunctionMetricsAggregator("stddev")
MonitorFormulaAndFunctionMetricsAggregator.COUNT_UNIQUE = MonitorFormulaAndFunctionMetricsAggregator("count_unique")
