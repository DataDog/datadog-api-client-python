# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class FormulaAndFunctionApmDependencyStatName(ModelSimple):
    """
    APM statistic.

    :param value: Must be one of ["avg_duration", "avg_root_duration", "avg_spans_per_trace", "error_rate", "pct_exec_time", "pct_of_traces", "total_traces_count"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "AVG_DURATION": "avg_duration",
            "AVG_ROOT_DURATION": "avg_root_duration",
            "AVG_SPANS_PER_TRACE": "avg_spans_per_trace",
            "ERROR_RATE": "error_rate",
            "PCT_EXEC_TIME": "pct_exec_time",
            "PCT_OF_TRACES": "pct_of_traces",
            "TOTAL_TRACES_COUNT": "total_traces_count",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
