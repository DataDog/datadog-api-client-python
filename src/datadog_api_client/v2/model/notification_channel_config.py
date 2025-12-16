# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class NotificationChannelConfig(ModelComposed):
    def __init__(self, **kwargs):
        """
        Defines the configuration for an On-Call notification channel

        :param formatted_number: The formatted international version of Number (e.g. +33 7 1 23 45 67).
        :type formatted_number: str

        :param number: The E-164 formatted phone number (e.g. +3371234567)
        :type number: str

        :param region: The ISO 3166-1 alpha-2 two-letter country code.
        :type region: str

        :param sms_subscribed_at: If present, the date the user subscribed this number to SMS messages
        :type sms_subscribed_at: datetime, none_type, optional

        :param type: Indicates that the notification channel is a phone
        :type type: NotificationChannelPhoneConfigType

        :param verified: Indicates whether this phone has been verified by the user in Datadog On-Call
        :type verified: bool

        :param address: The e-mail address to be notified
        :type address: str

        :param formats: Preferred content formats for notifications.
        :type formats: [NotificationChannelEmailFormatType]

        :param application_name: The name of the application used to receive push notifications
        :type application_name: str

        :param device_name: The name of the mobile device being used
        :type device_name: str
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
        from datadog_api_client.v2.model.notification_channel_phone_config import NotificationChannelPhoneConfig
        from datadog_api_client.v2.model.notification_channel_email_config import NotificationChannelEmailConfig
        from datadog_api_client.v2.model.notification_channel_push_config import NotificationChannelPushConfig

        return {
            "oneOf": [
                NotificationChannelPhoneConfig,
                NotificationChannelEmailConfig,
                NotificationChannelPushConfig,
            ],
        }
