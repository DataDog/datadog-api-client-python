# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleTypes(ModelSimple):
    """
    Security monitoring rule types.

    :param value: Must be one of ["application_security", "log_detection", "cloud_configuration", "infrastructure_configuration", "workload_security", "signal_correlation", "vulnerability_management"].
    :type value: str
    """

    allowed_values = {
        "application_security",
        "log_detection",
        "cloud_configuration",
        "infrastructure_configuration",
        "workload_security",
        "signal_correlation",
        "vulnerability_management",
    }
    APPLICATION_SECURITY: ClassVar["SecurityMonitoringRuleTypes"]
    LOG_DETECTION: ClassVar["SecurityMonitoringRuleTypes"]
    CLOUD_CONFIGURATION: ClassVar["SecurityMonitoringRuleTypes"]
    INFRASTRUCTURE_CONFIGURATION: ClassVar["SecurityMonitoringRuleTypes"]
    WORKLOAD_SECURITY: ClassVar["SecurityMonitoringRuleTypes"]
    SIGNAL_CORRELATION: ClassVar["SecurityMonitoringRuleTypes"]
    VULNERABILITY_MANAGEMENT: ClassVar["SecurityMonitoringRuleTypes"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleTypes.APPLICATION_SECURITY = SecurityMonitoringRuleTypes("application_security")
SecurityMonitoringRuleTypes.LOG_DETECTION = SecurityMonitoringRuleTypes("log_detection")
SecurityMonitoringRuleTypes.CLOUD_CONFIGURATION = SecurityMonitoringRuleTypes("cloud_configuration")
SecurityMonitoringRuleTypes.INFRASTRUCTURE_CONFIGURATION = SecurityMonitoringRuleTypes("infrastructure_configuration")
SecurityMonitoringRuleTypes.WORKLOAD_SECURITY = SecurityMonitoringRuleTypes("workload_security")
SecurityMonitoringRuleTypes.SIGNAL_CORRELATION = SecurityMonitoringRuleTypes("signal_correlation")
SecurityMonitoringRuleTypes.VULNERABILITY_MANAGEMENT = SecurityMonitoringRuleTypes("vulnerability_management")
