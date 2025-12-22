# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPhoneNotificationRuleMethod(ModelSimple):
    """
    Specifies the method in which a phone is used in a notification rule

    :param value: Must be one of ["sms", "voice"].
    :type value: str
    """

    allowed_values = {
        "sms",
        "voice",
    }
    SMS: ClassVar["OnCallPhoneNotificationRuleMethod"]
    VOICE: ClassVar["OnCallPhoneNotificationRuleMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPhoneNotificationRuleMethod.SMS = OnCallPhoneNotificationRuleMethod("sms")
OnCallPhoneNotificationRuleMethod.VOICE = OnCallPhoneNotificationRuleMethod("voice")
