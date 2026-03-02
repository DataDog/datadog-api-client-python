"""
Create an event email address returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.event_email_address_alert_type import EventEmailAddressAlertType
from datadog_api_client.v2.model.event_email_address_create_attributes import EventEmailAddressCreateAttributes
from datadog_api_client.v2.model.event_email_address_create_data import EventEmailAddressCreateData
from datadog_api_client.v2.model.event_email_address_create_request import EventEmailAddressCreateRequest
from datadog_api_client.v2.model.event_email_address_format import EventEmailAddressFormat
from datadog_api_client.v2.model.event_email_address_resource_type import EventEmailAddressResourceType

body = EventEmailAddressCreateRequest(
    data=EventEmailAddressCreateData(
        attributes=EventEmailAddressCreateAttributes(
            alert_type=EventEmailAddressAlertType.INFO,
            description="Email address for production alerts.",
            format=EventEmailAddressFormat.JSON,
            notify_handles=[
                "@slack-my-channel",
            ],
            tags=[
                "env:production",
                "team:my-team",
            ],
        ),
        type=EventEmailAddressResourceType.EVENT_EMAILS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_event_email_address"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_event_email_address(body=body)

    print(response)
