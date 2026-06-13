# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DataObservabilityMonitorRunStatus(ModelSimple):
    """
    The status of a data observability monitor run.

    :param value: Must be one of ["pending", "ok", "warn", "alert", "error"].
    :type value: str
    """

    allowed_values = {
        "pending",
        "ok",
        "warn",
        "alert",
        "error",
    }
    PENDING: ClassVar["DataObservabilityMonitorRunStatus"]
    OK: ClassVar["DataObservabilityMonitorRunStatus"]
    WARN: ClassVar["DataObservabilityMonitorRunStatus"]
    ALERT: ClassVar["DataObservabilityMonitorRunStatus"]
    ERROR: ClassVar["DataObservabilityMonitorRunStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DataObservabilityMonitorRunStatus.PENDING = DataObservabilityMonitorRunStatus("pending")
DataObservabilityMonitorRunStatus.OK = DataObservabilityMonitorRunStatus("ok")
DataObservabilityMonitorRunStatus.WARN = DataObservabilityMonitorRunStatus("warn")
DataObservabilityMonitorRunStatus.ALERT = DataObservabilityMonitorRunStatus("alert")
DataObservabilityMonitorRunStatus.ERROR = DataObservabilityMonitorRunStatus("error")
