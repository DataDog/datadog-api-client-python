# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleTypeCreate(ModelSimple):
    """
    The rule type.

    :param value: Must be one of ["application_security", "log_detection", "workload_security"].
    :type value: str
    """

    allowed_values = {
        "application_security",
        "log_detection",
        "workload_security",
    }
    APPLICATION_SECURITY: ClassVar["SecurityMonitoringRuleTypeCreate"]
    LOG_DETECTION: ClassVar["SecurityMonitoringRuleTypeCreate"]
    WORKLOAD_SECURITY: ClassVar["SecurityMonitoringRuleTypeCreate"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleTypeCreate.APPLICATION_SECURITY = SecurityMonitoringRuleTypeCreate("application_security")
SecurityMonitoringRuleTypeCreate.LOG_DETECTION = SecurityMonitoringRuleTypeCreate("log_detection")
SecurityMonitoringRuleTypeCreate.WORKLOAD_SECURITY = SecurityMonitoringRuleTypeCreate("workload_security")
