# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_phone_notification_rule_method import OnCallPhoneNotificationRuleMethod
    from datadog_api_client.v2.model.notification_channel_phone_config_type import NotificationChannelPhoneConfigType


class OnCallPhoneNotificationRuleSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_phone_notification_rule_method import OnCallPhoneNotificationRuleMethod
        from datadog_api_client.v2.model.notification_channel_phone_config_type import (
            NotificationChannelPhoneConfigType,
        )

        return {
            "method": (OnCallPhoneNotificationRuleMethod,),
            "type": (NotificationChannelPhoneConfigType,),
        }

    attribute_map = {
        "method": "method",
        "type": "type",
    }

    def __init__(self_, method: OnCallPhoneNotificationRuleMethod, type: NotificationChannelPhoneConfigType, **kwargs):
        """
        Configuration for using a phone notification channel in a notification rule

        :param method: Specifies the method in which a phone is used in a notification rule
        :type method: OnCallPhoneNotificationRuleMethod

        :param type: Indicates that the notification channel is a phone
        :type type: NotificationChannelPhoneConfigType
        """
        super().__init__(kwargs)

        self_.method = method
        self_.type = type
