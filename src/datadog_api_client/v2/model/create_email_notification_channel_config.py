# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.notification_channel_email_format_type import NotificationChannelEmailFormatType
    from datadog_api_client.v2.model.notification_channel_email_config_type import NotificationChannelEmailConfigType


class CreateEmailNotificationChannelConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_channel_email_format_type import (
            NotificationChannelEmailFormatType,
        )
        from datadog_api_client.v2.model.notification_channel_email_config_type import (
            NotificationChannelEmailConfigType,
        )

        return {
            "address": (str,),
            "formats": ([NotificationChannelEmailFormatType],),
            "type": (NotificationChannelEmailConfigType,),
        }

    attribute_map = {
        "address": "address",
        "formats": "formats",
        "type": "type",
    }

    def __init__(
        self_,
        address: str,
        formats: List[NotificationChannelEmailFormatType],
        type: NotificationChannelEmailConfigType,
        **kwargs,
    ):
        """
        Configuration to create an e-mail notification channel

        :param address: The e-mail address to be notified
        :type address: str

        :param formats: Preferred content formats for notifications.
        :type formats: [NotificationChannelEmailFormatType]

        :param type: Indicates that the notification channel is an e-mail address
        :type type: NotificationChannelEmailConfigType
        """
        super().__init__(kwargs)

        self_.address = address
        self_.formats = formats
        self_.type = type
