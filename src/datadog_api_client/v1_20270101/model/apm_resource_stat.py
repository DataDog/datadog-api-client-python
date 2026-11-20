# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApmResourceStat(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["errors", "error_rate", "latency_avg", "latency_max", "latency_p50", "latency_p75", "latency_p90", "latency_p95", "latency_p99", "latency_distribution", "hits", "total_time"].
    :type value: str
    """

    allowed_values = {
        "errors",
        "error_rate",
        "latency_avg",
        "latency_max",
        "latency_p50",
        "latency_p75",
        "latency_p90",
        "latency_p95",
        "latency_p99",
        "latency_distribution",
        "hits",
        "total_time",
    }
    ERRORS: ClassVar["ApmResourceStat"]
    ERROR_RATE: ClassVar["ApmResourceStat"]
    LATENCY_AVG: ClassVar["ApmResourceStat"]
    LATENCY_MAX: ClassVar["ApmResourceStat"]
    LATENCY_P50: ClassVar["ApmResourceStat"]
    LATENCY_P75: ClassVar["ApmResourceStat"]
    LATENCY_P90: ClassVar["ApmResourceStat"]
    LATENCY_P95: ClassVar["ApmResourceStat"]
    LATENCY_P99: ClassVar["ApmResourceStat"]
    LATENCY_DISTRIBUTION: ClassVar["ApmResourceStat"]
    HITS: ClassVar["ApmResourceStat"]
    TOTAL_TIME: ClassVar["ApmResourceStat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApmResourceStat.ERRORS = ApmResourceStat("errors")
ApmResourceStat.ERROR_RATE = ApmResourceStat("error_rate")
ApmResourceStat.LATENCY_AVG = ApmResourceStat("latency_avg")
ApmResourceStat.LATENCY_MAX = ApmResourceStat("latency_max")
ApmResourceStat.LATENCY_P50 = ApmResourceStat("latency_p50")
ApmResourceStat.LATENCY_P75 = ApmResourceStat("latency_p75")
ApmResourceStat.LATENCY_P90 = ApmResourceStat("latency_p90")
ApmResourceStat.LATENCY_P95 = ApmResourceStat("latency_p95")
ApmResourceStat.LATENCY_P99 = ApmResourceStat("latency_p99")
ApmResourceStat.LATENCY_DISTRIBUTION = ApmResourceStat("latency_distribution")
ApmResourceStat.HITS = ApmResourceStat("hits")
ApmResourceStat.TOTAL_TIME = ApmResourceStat("total_time")
