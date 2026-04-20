"""
Update an event email address returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.event_email_address_alert_type import EventEmailAddressAlertType
from datadog_api_client.v2.model.event_email_address_resource_type import EventEmailAddressResourceType
from datadog_api_client.v2.model.event_email_address_update_attributes import EventEmailAddressUpdateAttributes
from datadog_api_client.v2.model.event_email_address_update_data import EventEmailAddressUpdateData
from datadog_api_client.v2.model.event_email_address_update_request import EventEmailAddressUpdateRequest
from uuid import UUID

body = EventEmailAddressUpdateRequest(
    data=EventEmailAddressUpdateData(
        attributes=EventEmailAddressUpdateAttributes(
            alert_type=EventEmailAddressAlertType.INFO,
            description="Updated description for the email address.",
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
configuration.unstable_operations["update_event_email_address"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.update_event_email_address(
        email_uuid=UUID("00000000-0000-0000-0000-000000000001"), body=body
    )

    print(response)
