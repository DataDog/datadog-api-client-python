"""
Create on-call event email address returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.create_on_call_event_email_address_request import CreateOnCallEventEmailAddressRequest
from datadog_api_client.v2.model.create_on_call_event_email_address_request_data import (
    CreateOnCallEventEmailAddressRequestData,
)
from datadog_api_client.v2.model.create_on_call_event_email_address_request_data_attributes import (
    CreateOnCallEventEmailAddressRequestDataAttributes,
)
from datadog_api_client.v2.model.event_emails_type import EventEmailsType

body = CreateOnCallEventEmailAddressRequest(
    data=CreateOnCallEventEmailAddressRequestData(
        attributes=CreateOnCallEventEmailAddressRequestDataAttributes(
            format="",
            tags=[
                "",
            ],
        ),
        type=EventEmailsType.EVENT_EMAILS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_on_call_event_email_address"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_on_call_event_email_address(body=body)

    print(response)
