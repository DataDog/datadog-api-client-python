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
    from datadog_api_client.v2.model.notification_channel_phone_config_type import NotificationChannelPhoneConfigType


class CreatePhoneNotificationChannelConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_channel_phone_config_type import (
            NotificationChannelPhoneConfigType,
        )

        return {
            "number": (str,),
            "type": (NotificationChannelPhoneConfigType,),
        }

    attribute_map = {
        "number": "number",
        "type": "type",
    }

    def __init__(self_, number: str, type: NotificationChannelPhoneConfigType, **kwargs):
        """
        Configuration to create a phone notification channel

        :param number: The E-164 formatted phone number (e.g. +3371234567)
        :type number: str

        :param type: Indicates that the notification channel is a phone
        :type type: NotificationChannelPhoneConfigType
        """
        super().__init__(kwargs)

        self_.number = number
        self_.type = type
