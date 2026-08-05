# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ControlNotificationTargetType(ModelSimple):
    """
    The type of notification destination.

    :param value: Must be one of ["email", "slack", "at_mention", "case"].
    :type value: str
    """

    allowed_values = {
        "email",
        "slack",
        "at_mention",
        "case",
    }
    EMAIL: ClassVar["ControlNotificationTargetType"]
    SLACK: ClassVar["ControlNotificationTargetType"]
    AT_MENTION: ClassVar["ControlNotificationTargetType"]
    CASE: ClassVar["ControlNotificationTargetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ControlNotificationTargetType.EMAIL = ControlNotificationTargetType("email")
ControlNotificationTargetType.SLACK = ControlNotificationTargetType("slack")
ControlNotificationTargetType.AT_MENTION = ControlNotificationTargetType("at_mention")
ControlNotificationTargetType.CASE = ControlNotificationTargetType("case")
