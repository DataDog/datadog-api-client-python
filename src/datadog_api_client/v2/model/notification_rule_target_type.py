# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NotificationRuleTargetType(ModelSimple):
    """
    The type of notification target.

    :param value: Must be one of ["EMAIL", "SLACK_CHANNEL", "SLACK_USER", "WEBHOOK", "PAGERDUTY_SERVICE", "MS_TEAMS_CHANNEL"].
    :type value: str
    """

    allowed_values = {
        "EMAIL",
        "SLACK_CHANNEL",
        "SLACK_USER",
        "WEBHOOK",
        "PAGERDUTY_SERVICE",
        "MS_TEAMS_CHANNEL",
    }
    EMAIL: ClassVar["NotificationRuleTargetType"]
    SLACK_CHANNEL: ClassVar["NotificationRuleTargetType"]
    SLACK_USER: ClassVar["NotificationRuleTargetType"]
    WEBHOOK: ClassVar["NotificationRuleTargetType"]
    PAGERDUTY_SERVICE: ClassVar["NotificationRuleTargetType"]
    MS_TEAMS_CHANNEL: ClassVar["NotificationRuleTargetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotificationRuleTargetType.EMAIL = NotificationRuleTargetType("EMAIL")
NotificationRuleTargetType.SLACK_CHANNEL = NotificationRuleTargetType("SLACK_CHANNEL")
NotificationRuleTargetType.SLACK_USER = NotificationRuleTargetType("SLACK_USER")
NotificationRuleTargetType.WEBHOOK = NotificationRuleTargetType("WEBHOOK")
NotificationRuleTargetType.PAGERDUTY_SERVICE = NotificationRuleTargetType("PAGERDUTY_SERVICE")
NotificationRuleTargetType.MS_TEAMS_CHANNEL = NotificationRuleTargetType("MS_TEAMS_CHANNEL")
