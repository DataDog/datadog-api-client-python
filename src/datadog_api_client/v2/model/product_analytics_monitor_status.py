# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsMonitorStatus(ModelSimple):
    """
    Current alert status of the monitor. `No Data` is returned when the monitor has not been evaluated yet.

    :param value: Must be one of ["OK", "Alert", "Warn", "No Data"].
    :type value: str
    """

    allowed_values = {
        "OK",
        "Alert",
        "Warn",
        "No Data",
    }
    OK: ClassVar["ProductAnalyticsMonitorStatus"]
    ALERT: ClassVar["ProductAnalyticsMonitorStatus"]
    WARN: ClassVar["ProductAnalyticsMonitorStatus"]
    NO_DATA: ClassVar["ProductAnalyticsMonitorStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsMonitorStatus.OK = ProductAnalyticsMonitorStatus("OK")
ProductAnalyticsMonitorStatus.ALERT = ProductAnalyticsMonitorStatus("Alert")
ProductAnalyticsMonitorStatus.WARN = ProductAnalyticsMonitorStatus("Warn")
ProductAnalyticsMonitorStatus.NO_DATA = ProductAnalyticsMonitorStatus("No Data")
