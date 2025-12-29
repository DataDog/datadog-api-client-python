# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamNotificationRuleType(ModelSimple):
    """
    Team notification rule type

    :param value: If omitted defaults to "team_notification_rules". Must be one of ["team_notification_rules"].
    :type value: str
    """

    allowed_values = {
        "team_notification_rules",
    }
    TEAM_NOTIFICATION_RULES: ClassVar["TeamNotificationRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamNotificationRuleType.TEAM_NOTIFICATION_RULES = TeamNotificationRuleType("team_notification_rules")
