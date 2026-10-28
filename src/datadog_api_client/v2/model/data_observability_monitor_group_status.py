# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DataObservabilityMonitorGroupStatus(ModelSimple):
    """
    The state of a monitor group, from the alerting engine.

    :param value: Must be one of ["ok", "warn", "alert", "no_data", "unknown"].
    :type value: str
    """

    allowed_values = {
        "ok",
        "warn",
        "alert",
        "no_data",
        "unknown",
    }
    OK: ClassVar["DataObservabilityMonitorGroupStatus"]
    WARN: ClassVar["DataObservabilityMonitorGroupStatus"]
    ALERT: ClassVar["DataObservabilityMonitorGroupStatus"]
    NO_DATA: ClassVar["DataObservabilityMonitorGroupStatus"]
    UNKNOWN: ClassVar["DataObservabilityMonitorGroupStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DataObservabilityMonitorGroupStatus.OK = DataObservabilityMonitorGroupStatus("ok")
DataObservabilityMonitorGroupStatus.WARN = DataObservabilityMonitorGroupStatus("warn")
DataObservabilityMonitorGroupStatus.ALERT = DataObservabilityMonitorGroupStatus("alert")
DataObservabilityMonitorGroupStatus.NO_DATA = DataObservabilityMonitorGroupStatus("no_data")
DataObservabilityMonitorGroupStatus.UNKNOWN = DataObservabilityMonitorGroupStatus("unknown")
