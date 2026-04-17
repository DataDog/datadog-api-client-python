# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApmDependencyStatName(ModelSimple):
    """
    The APM dependency statistic to query.

    :param value: Must be one of ["avg_duration", "avg_root_duration", "avg_spans_per_trace", "error_rate", "pct_exec_time", "pct_of_traces", "total_traces_count"].
    :type value: str
    """

    allowed_values = {
        "avg_duration",
        "avg_root_duration",
        "avg_spans_per_trace",
        "error_rate",
        "pct_exec_time",
        "pct_of_traces",
        "total_traces_count",
    }
    AVG_DURATION: ClassVar["ApmDependencyStatName"]
    AVG_ROOT_DURATION: ClassVar["ApmDependencyStatName"]
    AVG_SPANS_PER_TRACE: ClassVar["ApmDependencyStatName"]
    ERROR_RATE: ClassVar["ApmDependencyStatName"]
    PCT_EXEC_TIME: ClassVar["ApmDependencyStatName"]
    PCT_OF_TRACES: ClassVar["ApmDependencyStatName"]
    TOTAL_TRACES_COUNT: ClassVar["ApmDependencyStatName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApmDependencyStatName.AVG_DURATION = ApmDependencyStatName("avg_duration")
ApmDependencyStatName.AVG_ROOT_DURATION = ApmDependencyStatName("avg_root_duration")
ApmDependencyStatName.AVG_SPANS_PER_TRACE = ApmDependencyStatName("avg_spans_per_trace")
ApmDependencyStatName.ERROR_RATE = ApmDependencyStatName("error_rate")
ApmDependencyStatName.PCT_EXEC_TIME = ApmDependencyStatName("pct_exec_time")
ApmDependencyStatName.PCT_OF_TRACES = ApmDependencyStatName("pct_of_traces")
ApmDependencyStatName.TOTAL_TRACES_COUNT = ApmDependencyStatName("total_traces_count")
