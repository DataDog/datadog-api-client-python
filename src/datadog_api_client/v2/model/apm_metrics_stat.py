# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApmMetricsStat(ModelSimple):
    """
    The APM metric statistic to query.

    :param value: Must be one of ["error_rate", "errors", "errors_per_second", "hits", "hits_per_second", "apdex", "latency_avg", "latency_max", "latency_p50", "latency_p75", "latency_p90", "latency_p95", "latency_p99", "latency_p999", "latency_distribution", "total_time"].
    :type value: str
    """

    allowed_values = {
        "error_rate",
        "errors",
        "errors_per_second",
        "hits",
        "hits_per_second",
        "apdex",
        "latency_avg",
        "latency_max",
        "latency_p50",
        "latency_p75",
        "latency_p90",
        "latency_p95",
        "latency_p99",
        "latency_p999",
        "latency_distribution",
        "total_time",
    }
    ERROR_RATE: ClassVar["ApmMetricsStat"]
    ERRORS: ClassVar["ApmMetricsStat"]
    ERRORS_PER_SECOND: ClassVar["ApmMetricsStat"]
    HITS: ClassVar["ApmMetricsStat"]
    HITS_PER_SECOND: ClassVar["ApmMetricsStat"]
    APDEX: ClassVar["ApmMetricsStat"]
    LATENCY_AVG: ClassVar["ApmMetricsStat"]
    LATENCY_MAX: ClassVar["ApmMetricsStat"]
    LATENCY_P50: ClassVar["ApmMetricsStat"]
    LATENCY_P75: ClassVar["ApmMetricsStat"]
    LATENCY_P90: ClassVar["ApmMetricsStat"]
    LATENCY_P95: ClassVar["ApmMetricsStat"]
    LATENCY_P99: ClassVar["ApmMetricsStat"]
    LATENCY_P999: ClassVar["ApmMetricsStat"]
    LATENCY_DISTRIBUTION: ClassVar["ApmMetricsStat"]
    TOTAL_TIME: ClassVar["ApmMetricsStat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApmMetricsStat.ERROR_RATE = ApmMetricsStat("error_rate")
ApmMetricsStat.ERRORS = ApmMetricsStat("errors")
ApmMetricsStat.ERRORS_PER_SECOND = ApmMetricsStat("errors_per_second")
ApmMetricsStat.HITS = ApmMetricsStat("hits")
ApmMetricsStat.HITS_PER_SECOND = ApmMetricsStat("hits_per_second")
ApmMetricsStat.APDEX = ApmMetricsStat("apdex")
ApmMetricsStat.LATENCY_AVG = ApmMetricsStat("latency_avg")
ApmMetricsStat.LATENCY_MAX = ApmMetricsStat("latency_max")
ApmMetricsStat.LATENCY_P50 = ApmMetricsStat("latency_p50")
ApmMetricsStat.LATENCY_P75 = ApmMetricsStat("latency_p75")
ApmMetricsStat.LATENCY_P90 = ApmMetricsStat("latency_p90")
ApmMetricsStat.LATENCY_P95 = ApmMetricsStat("latency_p95")
ApmMetricsStat.LATENCY_P99 = ApmMetricsStat("latency_p99")
ApmMetricsStat.LATENCY_P999 = ApmMetricsStat("latency_p999")
ApmMetricsStat.LATENCY_DISTRIBUTION = ApmMetricsStat("latency_distribution")
ApmMetricsStat.TOTAL_TIME = ApmMetricsStat("total_time")
