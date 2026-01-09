# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringCriticalAssetSeverity(ModelSimple):
    """
    Severity associated with this critical asset. Either an explicit severity can be set, or the severity can be increased or decreased.

    :param value: Must be one of ["info", "low", "medium", "high", "critical", "increase", "decrease"].
    :type value: str
    """

    allowed_values = {
        "info",
        "low",
        "medium",
        "high",
        "critical",
        "increase",
        "decrease",
    }
    INFO: ClassVar["SecurityMonitoringCriticalAssetSeverity"]
    LOW: ClassVar["SecurityMonitoringCriticalAssetSeverity"]
    MEDIUM: ClassVar["SecurityMonitoringCriticalAssetSeverity"]
    HIGH: ClassVar["SecurityMonitoringCriticalAssetSeverity"]
    CRITICAL: ClassVar["SecurityMonitoringCriticalAssetSeverity"]
    INCREASE: ClassVar["SecurityMonitoringCriticalAssetSeverity"]
    DECREASE: ClassVar["SecurityMonitoringCriticalAssetSeverity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringCriticalAssetSeverity.INFO = SecurityMonitoringCriticalAssetSeverity("info")
SecurityMonitoringCriticalAssetSeverity.LOW = SecurityMonitoringCriticalAssetSeverity("low")
SecurityMonitoringCriticalAssetSeverity.MEDIUM = SecurityMonitoringCriticalAssetSeverity("medium")
SecurityMonitoringCriticalAssetSeverity.HIGH = SecurityMonitoringCriticalAssetSeverity("high")
SecurityMonitoringCriticalAssetSeverity.CRITICAL = SecurityMonitoringCriticalAssetSeverity("critical")
SecurityMonitoringCriticalAssetSeverity.INCREASE = SecurityMonitoringCriticalAssetSeverity("increase")
SecurityMonitoringCriticalAssetSeverity.DECREASE = SecurityMonitoringCriticalAssetSeverity("decrease")
