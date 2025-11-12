"""
Update an On-Call email for a user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.email_attributes import EmailAttributes
from datadog_api_client.v2.model.email_data import EmailData
from datadog_api_client.v2.model.email_format_type import EmailFormatType
from datadog_api_client.v2.model.email_type import EmailType
from datadog_api_client.v2.model.email_update_request import EmailUpdateRequest

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "oncall_email" in the system
ONCALL_EMAIL_DATA_ATTRIBUTES_ADDRESS = environ["ONCALL_EMAIL_DATA_ATTRIBUTES_ADDRESS"]
ONCALL_EMAIL_DATA_ID = environ["ONCALL_EMAIL_DATA_ID"]

body = EmailUpdateRequest(
    data=EmailData(
        id=ONCALL_EMAIL_DATA_ID,
        attributes=EmailAttributes(
            active=True,
            address=ONCALL_EMAIL_DATA_ATTRIBUTES_ADDRESS,
            alias="Example-On-Call-alias",
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
    response = api_instance.update_user_email_notification_channel(
        user_id=USER_DATA_ID, email_id=ONCALL_EMAIL_DATA_ID, body=body
    )

    print(response)
