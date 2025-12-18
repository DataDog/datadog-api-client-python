# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallNotificationRuleCategory(ModelSimple):
    """
    Specifies the category a notification rule will apply to

    :param value: If omitted defaults to "high_urgency". Must be one of ["high_urgency", "low_urgency"].
    :type value: str
    """

    allowed_values = {
        "high_urgency",
        "low_urgency",
    }
    HIGH_URGENCY: ClassVar["OnCallNotificationRuleCategory"]
    LOW_URGENCY: ClassVar["OnCallNotificationRuleCategory"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallNotificationRuleCategory.HIGH_URGENCY = OnCallNotificationRuleCategory("high_urgency")
OnCallNotificationRuleCategory.LOW_URGENCY = OnCallNotificationRuleCategory("low_urgency")
