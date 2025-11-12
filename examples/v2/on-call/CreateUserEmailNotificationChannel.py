"""
Create an On-Call email for a user returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.email_attributes import EmailAttributes
from datadog_api_client.v2.model.email_create_request import EmailCreateRequest
from datadog_api_client.v2.model.email_data import EmailData
from datadog_api_client.v2.model.email_format_type import EmailFormatType
from datadog_api_client.v2.model.email_type import EmailType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = EmailCreateRequest(
    data=EmailData(
        attributes=EmailAttributes(
            active=True,
            address="john.doe@datadoghq.com",
            alias="",
            formats=[
                EmailFormatType.HTML,
            ],
        ),
        type=EmailType.EMAILS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.create_user_email_notification_channel(user_id=USER_DATA_ID, body=body)

    print(response)
