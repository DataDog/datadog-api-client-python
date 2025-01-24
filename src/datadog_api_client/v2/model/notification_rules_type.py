# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NotificationRulesType(ModelSimple):
    """
    The rule type associated to notification rules.

    :param value: If omitted defaults to "notification_rules". Must be one of ["notification_rules"].
    :type value: str
    """

    allowed_values = {
        "notification_rules",
    }
    NOTIFICATION_RULES: ClassVar["NotificationRulesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotificationRulesType.NOTIFICATION_RULES = NotificationRulesType("notification_rules")
