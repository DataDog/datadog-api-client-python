# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorNotificationRuleResourceType(ModelSimple):
    """
    Monitor notification rule resource type.

    :param value: If omitted defaults to "monitor-notification-rule". Must be one of ["monitor-notification-rule"].
    :type value: str
    """

    allowed_values = {
        "monitor-notification-rule",
    }
    MONITOR_NOTIFICATION_RULE: ClassVar["MonitorNotificationRuleResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE = MonitorNotificationRuleResourceType(
    "monitor-notification-rule"
)
