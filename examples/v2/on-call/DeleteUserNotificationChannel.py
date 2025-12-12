"""
Delete an On-Call notification channel for a user returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "oncall_email_notification_channel" in the system
ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID = environ["ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    api_instance.delete_user_notification_channel(
        user_id=USER_DATA_ID,
        channel_id=ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID,
    )
