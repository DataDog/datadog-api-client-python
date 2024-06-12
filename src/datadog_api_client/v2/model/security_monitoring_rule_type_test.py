# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleTypeTest(ModelSimple):
    """
    The rule type.

    :param value: If omitted defaults to "log_detection". Must be one of ["log_detection"].
    :type value: str
    """

    allowed_values = {
        "log_detection",
    }
    LOG_DETECTION: ClassVar["SecurityMonitoringRuleTypeTest"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleTypeTest.LOG_DETECTION = SecurityMonitoringRuleTypeTest("log_detection")
