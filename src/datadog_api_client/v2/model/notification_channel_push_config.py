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
    from datadog_api_client.v2.model.notification_channel_push_config_type import NotificationChannelPushConfigType


class NotificationChannelPushConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_channel_push_config_type import NotificationChannelPushConfigType

        return {
            "application_name": (str,),
            "device_name": (str,),
            "type": (NotificationChannelPushConfigType,),
        }

    attribute_map = {
        "application_name": "application_name",
        "device_name": "device_name",
        "type": "type",
    }

    def __init__(self_, application_name: str, device_name: str, type: NotificationChannelPushConfigType, **kwargs):
        """
        Push notification channel configuration

        :param application_name: The name of the application used to receive push notifications
        :type application_name: str

        :param device_name: The name of the mobile device being used
        :type device_name: str

        :param type: Indicates that the notification channel is a mobile device for push notifications
        :type type: NotificationChannelPushConfigType
        """
        super().__init__(kwargs)

        self_.application_name = application_name
        self_.device_name = device_name
        self_.type = type
