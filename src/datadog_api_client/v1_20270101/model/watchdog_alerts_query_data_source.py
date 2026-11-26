# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WatchdogAlertsQueryDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "watchdog_alerts". Must be one of ["watchdog_alerts"].
    :type value: str
    """

    allowed_values = {
        "watchdog_alerts",
    }
    WATCHDOG_ALERTS: ClassVar["WatchdogAlertsQueryDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WatchdogAlertsQueryDataSource.WATCHDOG_ALERTS = WatchdogAlertsQueryDataSource("watchdog_alerts")
