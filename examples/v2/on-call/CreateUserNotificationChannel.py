"""
Create an On-Call notification channel for a user returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.create_email_notification_channel_config import CreateEmailNotificationChannelConfig
from datadog_api_client.v2.model.create_notification_channel_attributes import CreateNotificationChannelAttributes
from datadog_api_client.v2.model.create_notification_channel_data import CreateNotificationChannelData
from datadog_api_client.v2.model.create_user_notification_channel_request import CreateUserNotificationChannelRequest
from datadog_api_client.v2.model.notification_channel_email_config_type import NotificationChannelEmailConfigType
from datadog_api_client.v2.model.notification_channel_email_format_type import NotificationChannelEmailFormatType
from datadog_api_client.v2.model.notification_channel_type import NotificationChannelType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = CreateUserNotificationChannelRequest(
    data=CreateNotificationChannelData(
        attributes=CreateNotificationChannelAttributes(
            config=CreateEmailNotificationChannelConfig(
                address="foo@bar.com",
                formats=[
                    NotificationChannelEmailFormatType.HTML,
                ],
                type=NotificationChannelEmailConfigType.EMAIL,
            ),
        ),
        type=NotificationChannelType.NOTIFICATION_CHANNELS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.create_user_notification_channel(user_id=USER_DATA_ID, body=body)

    print(response)
