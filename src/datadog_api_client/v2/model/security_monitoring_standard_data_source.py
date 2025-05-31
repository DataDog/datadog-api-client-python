# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringStandardDataSource(ModelSimple):
    """
    Source of events, either logs, audit trail, or Datadog events.

    :param value: If omitted defaults to "logs". Must be one of ["logs", "audit", "app_sec_spans", "spans", "security_runtime", "network", "events"].
    :type value: str
    """

    allowed_values = {
        "logs",
        "audit",
        "app_sec_spans",
        "spans",
        "security_runtime",
        "network",
        "events",
    }
    LOGS: ClassVar["SecurityMonitoringStandardDataSource"]
    AUDIT: ClassVar["SecurityMonitoringStandardDataSource"]
    APP_SEC_SPANS: ClassVar["SecurityMonitoringStandardDataSource"]
    SPANS: ClassVar["SecurityMonitoringStandardDataSource"]
    SECURITY_RUNTIME: ClassVar["SecurityMonitoringStandardDataSource"]
    NETWORK: ClassVar["SecurityMonitoringStandardDataSource"]
    EVENTS: ClassVar["SecurityMonitoringStandardDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringStandardDataSource.LOGS = SecurityMonitoringStandardDataSource("logs")
SecurityMonitoringStandardDataSource.AUDIT = SecurityMonitoringStandardDataSource("audit")
SecurityMonitoringStandardDataSource.APP_SEC_SPANS = SecurityMonitoringStandardDataSource("app_sec_spans")
SecurityMonitoringStandardDataSource.SPANS = SecurityMonitoringStandardDataSource("spans")
SecurityMonitoringStandardDataSource.SECURITY_RUNTIME = SecurityMonitoringStandardDataSource("security_runtime")
SecurityMonitoringStandardDataSource.NETWORK = SecurityMonitoringStandardDataSource("network")
SecurityMonitoringStandardDataSource.EVENTS = SecurityMonitoringStandardDataSource("events")
