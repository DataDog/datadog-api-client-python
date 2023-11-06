# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SecurityMonitoringRuleTypeCreate(StringEnum):
    """
    The rule type.

    :param value: Must be one of ["log_detection", "workload_security"].
    :type value: str
    """

    allowed_values = {
        "log_detection",
        "workload_security",
    }
    LOG_DETECTION: ClassVar["SecurityMonitoringRuleTypeCreate"]
    WORKLOAD_SECURITY: ClassVar["SecurityMonitoringRuleTypeCreate"]


SecurityMonitoringRuleTypeCreate.LOG_DETECTION = SecurityMonitoringRuleTypeCreate("log_detection")
SecurityMonitoringRuleTypeCreate.WORKLOAD_SECURITY = SecurityMonitoringRuleTypeCreate("workload_security")
