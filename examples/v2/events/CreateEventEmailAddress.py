"""
Create event email address returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.create_event_email_address_request import CreateEventEmailAddressRequest
from datadog_api_client.v2.model.create_event_email_address_request_data import CreateEventEmailAddressRequestData
from datadog_api_client.v2.model.create_event_email_address_request_data_attributes import (
    CreateEventEmailAddressRequestDataAttributes,
)
from datadog_api_client.v2.model.event_emails_type import EventEmailsType

body = CreateEventEmailAddressRequest(
    data=CreateEventEmailAddressRequestData(
        attributes=CreateEventEmailAddressRequestDataAttributes(
            format="",
            notify_handles=[
                "",
            ],
            tags=[
                "",
            ],
        ),
        type=EventEmailsType.EVENT_EMAILS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_event_email_address"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_event_email_address(body=body)

    print(response)
