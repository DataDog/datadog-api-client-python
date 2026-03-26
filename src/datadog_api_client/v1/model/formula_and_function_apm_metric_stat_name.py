# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormulaAndFunctionApmMetricStatName(ModelSimple):
    """
    APM metric stat name.

    :param value: Must be one of ["errors", "error_rate", "errors_per_second", "latency_avg", "latency_max", "latency_p50", "latency_p75", "latency_p90", "latency_p95", "latency_p99", "latency_p999", "latency_distribution", "hits", "hits_per_second", "total_time", "apdex"].
    :type value: str
    """

    allowed_values = {
        "errors",
        "error_rate",
        "errors_per_second",
        "latency_avg",
        "latency_max",
        "latency_p50",
        "latency_p75",
        "latency_p90",
        "latency_p95",
        "latency_p99",
        "latency_p999",
        "latency_distribution",
        "hits",
        "hits_per_second",
        "total_time",
        "apdex",
    }
    ERRORS: ClassVar["FormulaAndFunctionApmMetricStatName"]
    ERROR_RATE: ClassVar["FormulaAndFunctionApmMetricStatName"]
    ERRORS_PER_SECOND: ClassVar["FormulaAndFunctionApmMetricStatName"]
    LATENCY_AVG: ClassVar["FormulaAndFunctionApmMetricStatName"]
    LATENCY_MAX: ClassVar["FormulaAndFunctionApmMetricStatName"]
    LATENCY_P50: ClassVar["FormulaAndFunctionApmMetricStatName"]
    LATENCY_P75: ClassVar["FormulaAndFunctionApmMetricStatName"]
    LATENCY_P90: ClassVar["FormulaAndFunctionApmMetricStatName"]
    LATENCY_P95: ClassVar["FormulaAndFunctionApmMetricStatName"]
    LATENCY_P99: ClassVar["FormulaAndFunctionApmMetricStatName"]
    LATENCY_P999: ClassVar["FormulaAndFunctionApmMetricStatName"]
    LATENCY_DISTRIBUTION: ClassVar["FormulaAndFunctionApmMetricStatName"]
    HITS: ClassVar["FormulaAndFunctionApmMetricStatName"]
    HITS_PER_SECOND: ClassVar["FormulaAndFunctionApmMetricStatName"]
    TOTAL_TIME: ClassVar["FormulaAndFunctionApmMetricStatName"]
    APDEX: ClassVar["FormulaAndFunctionApmMetricStatName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormulaAndFunctionApmMetricStatName.ERRORS = FormulaAndFunctionApmMetricStatName("errors")
FormulaAndFunctionApmMetricStatName.ERROR_RATE = FormulaAndFunctionApmMetricStatName("error_rate")
FormulaAndFunctionApmMetricStatName.ERRORS_PER_SECOND = FormulaAndFunctionApmMetricStatName("errors_per_second")
FormulaAndFunctionApmMetricStatName.LATENCY_AVG = FormulaAndFunctionApmMetricStatName("latency_avg")
FormulaAndFunctionApmMetricStatName.LATENCY_MAX = FormulaAndFunctionApmMetricStatName("latency_max")
FormulaAndFunctionApmMetricStatName.LATENCY_P50 = FormulaAndFunctionApmMetricStatName("latency_p50")
FormulaAndFunctionApmMetricStatName.LATENCY_P75 = FormulaAndFunctionApmMetricStatName("latency_p75")
FormulaAndFunctionApmMetricStatName.LATENCY_P90 = FormulaAndFunctionApmMetricStatName("latency_p90")
FormulaAndFunctionApmMetricStatName.LATENCY_P95 = FormulaAndFunctionApmMetricStatName("latency_p95")
FormulaAndFunctionApmMetricStatName.LATENCY_P99 = FormulaAndFunctionApmMetricStatName("latency_p99")
FormulaAndFunctionApmMetricStatName.LATENCY_P999 = FormulaAndFunctionApmMetricStatName("latency_p999")
FormulaAndFunctionApmMetricStatName.LATENCY_DISTRIBUTION = FormulaAndFunctionApmMetricStatName("latency_distribution")
FormulaAndFunctionApmMetricStatName.HITS = FormulaAndFunctionApmMetricStatName("hits")
FormulaAndFunctionApmMetricStatName.HITS_PER_SECOND = FormulaAndFunctionApmMetricStatName("hits_per_second")
FormulaAndFunctionApmMetricStatName.TOTAL_TIME = FormulaAndFunctionApmMetricStatName("total_time")
FormulaAndFunctionApmMetricStatName.APDEX = FormulaAndFunctionApmMetricStatName("apdex")
