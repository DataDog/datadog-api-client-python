# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CreateNotificationChannelConfig(ModelComposed):
    def __init__(self, **kwargs):
        """
        Defines the configuration for creating an On-Call notification channel

        :param number: The E-164 formatted phone number (e.g. +3371234567)
        :type number: str

        :param type: Indicates that the notification channel is a phone
        :type type: NotificationChannelPhoneConfigType

        :param address: The e-mail address to be notified
        :type address: str

        :param formats: Preferred content formats for notifications.
        :type formats: [NotificationChannelEmailFormatType]
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.create_phone_notification_channel_config import (
            CreatePhoneNotificationChannelConfig,
        )
        from datadog_api_client.v2.model.create_email_notification_channel_config import (
            CreateEmailNotificationChannelConfig,
        )

        return {
            "oneOf": [
                CreatePhoneNotificationChannelConfig,
                CreateEmailNotificationChannelConfig,
            ],
        }
