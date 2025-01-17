# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionCostAggregator(ModelSimple):
    """
    Aggregation methods for metric queries.

    :param value: Must be one of ["avg", "sum", "max", "min", "last", "area", "l2norm", "percentile", "stddev"].
    :type value: str
    """

    allowed_values = {
        "avg",
        "sum",
        "max",
        "min",
        "last",
        "area",
        "l2norm",
        "percentile",
        "stddev",
    }
    AVG: ClassVar["MonitorFormulaAndFunctionCostAggregator"]
    SUM: ClassVar["MonitorFormulaAndFunctionCostAggregator"]
    MAX: ClassVar["MonitorFormulaAndFunctionCostAggregator"]
    MIN: ClassVar["MonitorFormulaAndFunctionCostAggregator"]
    LAST: ClassVar["MonitorFormulaAndFunctionCostAggregator"]
    AREA: ClassVar["MonitorFormulaAndFunctionCostAggregator"]
    L2NORM: ClassVar["MonitorFormulaAndFunctionCostAggregator"]
    PERCENTILE: ClassVar["MonitorFormulaAndFunctionCostAggregator"]
    STDDEV: ClassVar["MonitorFormulaAndFunctionCostAggregator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionCostAggregator.AVG = MonitorFormulaAndFunctionCostAggregator("avg")
MonitorFormulaAndFunctionCostAggregator.SUM = MonitorFormulaAndFunctionCostAggregator("sum")
MonitorFormulaAndFunctionCostAggregator.MAX = MonitorFormulaAndFunctionCostAggregator("max")
MonitorFormulaAndFunctionCostAggregator.MIN = MonitorFormulaAndFunctionCostAggregator("min")
MonitorFormulaAndFunctionCostAggregator.LAST = MonitorFormulaAndFunctionCostAggregator("last")
MonitorFormulaAndFunctionCostAggregator.AREA = MonitorFormulaAndFunctionCostAggregator("area")
MonitorFormulaAndFunctionCostAggregator.L2NORM = MonitorFormulaAndFunctionCostAggregator("l2norm")
MonitorFormulaAndFunctionCostAggregator.PERCENTILE = MonitorFormulaAndFunctionCostAggregator("percentile")
MonitorFormulaAndFunctionCostAggregator.STDDEV = MonitorFormulaAndFunctionCostAggregator("stddev")
