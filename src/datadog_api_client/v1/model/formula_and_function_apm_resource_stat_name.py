# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class FormulaAndFunctionApmResourceStatName(ModelSimple):
    """
    APM resource stat name.

    :param value: Must be one of ["errors", "error_rate", "hits", "latency_avg", "latency_distribution", "latency_max", "latency_p50", "latency_p75", "latency_p90", "latency_p95", "latency_p99"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "ERRORS": "errors",
            "ERROR_RATE": "error_rate",
            "HITS": "hits",
            "LATENCY_AVG": "latency_avg",
            "LATENCY_DISTRIBUTION": "latency_distribution",
            "LATENCY_MAX": "latency_max",
            "LATENCY_P50": "latency_p50",
            "LATENCY_P75": "latency_p75",
            "LATENCY_P90": "latency_p90",
            "LATENCY_P95": "latency_p95",
            "LATENCY_P99": "latency_p99",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
