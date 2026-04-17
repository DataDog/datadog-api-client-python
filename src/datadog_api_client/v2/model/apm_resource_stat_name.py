# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApmResourceStatName(ModelSimple):
    """
    The APM resource statistic to query.

    :param value: Must be one of ["error_rate", "errors", "hits", "latency_avg", "latency_max", "latency_p50", "latency_p75", "latency_p90", "latency_p95", "latency_p99", "latency_distribution", "total_time"].
    :type value: str
    """

    allowed_values = {
        "error_rate",
        "errors",
        "hits",
        "latency_avg",
        "latency_max",
        "latency_p50",
        "latency_p75",
        "latency_p90",
        "latency_p95",
        "latency_p99",
        "latency_distribution",
        "total_time",
    }
    ERROR_RATE: ClassVar["ApmResourceStatName"]
    ERRORS: ClassVar["ApmResourceStatName"]
    HITS: ClassVar["ApmResourceStatName"]
    LATENCY_AVG: ClassVar["ApmResourceStatName"]
    LATENCY_MAX: ClassVar["ApmResourceStatName"]
    LATENCY_P50: ClassVar["ApmResourceStatName"]
    LATENCY_P75: ClassVar["ApmResourceStatName"]
    LATENCY_P90: ClassVar["ApmResourceStatName"]
    LATENCY_P95: ClassVar["ApmResourceStatName"]
    LATENCY_P99: ClassVar["ApmResourceStatName"]
    LATENCY_DISTRIBUTION: ClassVar["ApmResourceStatName"]
    TOTAL_TIME: ClassVar["ApmResourceStatName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApmResourceStatName.ERROR_RATE = ApmResourceStatName("error_rate")
ApmResourceStatName.ERRORS = ApmResourceStatName("errors")
ApmResourceStatName.HITS = ApmResourceStatName("hits")
ApmResourceStatName.LATENCY_AVG = ApmResourceStatName("latency_avg")
ApmResourceStatName.LATENCY_MAX = ApmResourceStatName("latency_max")
ApmResourceStatName.LATENCY_P50 = ApmResourceStatName("latency_p50")
ApmResourceStatName.LATENCY_P75 = ApmResourceStatName("latency_p75")
ApmResourceStatName.LATENCY_P90 = ApmResourceStatName("latency_p90")
ApmResourceStatName.LATENCY_P95 = ApmResourceStatName("latency_p95")
ApmResourceStatName.LATENCY_P99 = ApmResourceStatName("latency_p99")
ApmResourceStatName.LATENCY_DISTRIBUTION = ApmResourceStatName("latency_distribution")
ApmResourceStatName.TOTAL_TIME = ApmResourceStatName("total_time")
