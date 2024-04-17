# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringNotificationRuleType(ModelSimple):
    """
    The type of the resource. The value should always be `notification_rules`.

    :param value: If omitted defaults to "notification_rules". Must be one of ["notification_rules"].
    :type value: str
    """

    allowed_values = {
        "notification_rules",
    }
    NOTIFICATION_RULES: ClassVar["SecurityMonitoringNotificationRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringNotificationRuleType.NOTIFICATION_RULES = SecurityMonitoringNotificationRuleType("notification_rules")
