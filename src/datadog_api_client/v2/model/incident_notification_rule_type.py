# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentNotificationRuleType(ModelSimple):
    """
    Notification rules resource type.

    :param value: If omitted defaults to "incident_notification_rules". Must be one of ["incident_notification_rules"].
    :type value: str
    """

    allowed_values = {
        "incident_notification_rules",
    }
    INCIDENT_NOTIFICATION_RULES: ClassVar["IncidentNotificationRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentNotificationRuleType.INCIDENT_NOTIFICATION_RULES = IncidentNotificationRuleType("incident_notification_rules")
