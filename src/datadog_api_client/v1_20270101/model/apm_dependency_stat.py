# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApmDependencyStat(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["error_rate", "avg_duration", "avg_root_duration", "avg_spans_per_trace", "pct_exec_time", "pct_of_traces", "total_traces_count"].
    :type value: str
    """

    allowed_values = {
        "error_rate",
        "avg_duration",
        "avg_root_duration",
        "avg_spans_per_trace",
        "pct_exec_time",
        "pct_of_traces",
        "total_traces_count",
    }
    ERROR_RATE: ClassVar["ApmDependencyStat"]
    AVG_DURATION: ClassVar["ApmDependencyStat"]
    AVG_ROOT_DURATION: ClassVar["ApmDependencyStat"]
    AVG_SPANS_PER_TRACE: ClassVar["ApmDependencyStat"]
    PCT_EXEC_TIME: ClassVar["ApmDependencyStat"]
    PCT_OF_TRACES: ClassVar["ApmDependencyStat"]
    TOTAL_TRACES_COUNT: ClassVar["ApmDependencyStat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApmDependencyStat.ERROR_RATE = ApmDependencyStat("error_rate")
ApmDependencyStat.AVG_DURATION = ApmDependencyStat("avg_duration")
ApmDependencyStat.AVG_ROOT_DURATION = ApmDependencyStat("avg_root_duration")
ApmDependencyStat.AVG_SPANS_PER_TRACE = ApmDependencyStat("avg_spans_per_trace")
ApmDependencyStat.PCT_EXEC_TIME = ApmDependencyStat("pct_exec_time")
ApmDependencyStat.PCT_OF_TRACES = ApmDependencyStat("pct_of_traces")
ApmDependencyStat.TOTAL_TRACES_COUNT = ApmDependencyStat("total_traces_count")
