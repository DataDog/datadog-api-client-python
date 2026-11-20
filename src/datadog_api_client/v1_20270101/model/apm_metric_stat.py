# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApmMetricStat(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

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
    ERRORS: ClassVar["ApmMetricStat"]
    ERROR_RATE: ClassVar["ApmMetricStat"]
    ERRORS_PER_SECOND: ClassVar["ApmMetricStat"]
    LATENCY_AVG: ClassVar["ApmMetricStat"]
    LATENCY_MAX: ClassVar["ApmMetricStat"]
    LATENCY_P50: ClassVar["ApmMetricStat"]
    LATENCY_P75: ClassVar["ApmMetricStat"]
    LATENCY_P90: ClassVar["ApmMetricStat"]
    LATENCY_P95: ClassVar["ApmMetricStat"]
    LATENCY_P99: ClassVar["ApmMetricStat"]
    LATENCY_P999: ClassVar["ApmMetricStat"]
    LATENCY_DISTRIBUTION: ClassVar["ApmMetricStat"]
    HITS: ClassVar["ApmMetricStat"]
    HITS_PER_SECOND: ClassVar["ApmMetricStat"]
    TOTAL_TIME: ClassVar["ApmMetricStat"]
    APDEX: ClassVar["ApmMetricStat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApmMetricStat.ERRORS = ApmMetricStat("errors")
ApmMetricStat.ERROR_RATE = ApmMetricStat("error_rate")
ApmMetricStat.ERRORS_PER_SECOND = ApmMetricStat("errors_per_second")
ApmMetricStat.LATENCY_AVG = ApmMetricStat("latency_avg")
ApmMetricStat.LATENCY_MAX = ApmMetricStat("latency_max")
ApmMetricStat.LATENCY_P50 = ApmMetricStat("latency_p50")
ApmMetricStat.LATENCY_P75 = ApmMetricStat("latency_p75")
ApmMetricStat.LATENCY_P90 = ApmMetricStat("latency_p90")
ApmMetricStat.LATENCY_P95 = ApmMetricStat("latency_p95")
ApmMetricStat.LATENCY_P99 = ApmMetricStat("latency_p99")
ApmMetricStat.LATENCY_P999 = ApmMetricStat("latency_p999")
ApmMetricStat.LATENCY_DISTRIBUTION = ApmMetricStat("latency_distribution")
ApmMetricStat.HITS = ApmMetricStat("hits")
ApmMetricStat.HITS_PER_SECOND = ApmMetricStat("hits_per_second")
ApmMetricStat.TOTAL_TIME = ApmMetricStat("total_time")
ApmMetricStat.APDEX = ApmMetricStat("apdex")
