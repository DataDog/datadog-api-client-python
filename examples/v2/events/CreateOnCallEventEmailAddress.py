"""
Create an on-call event email address returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.event_email_address_alert_type import EventEmailAddressAlertType
from datadog_api_client.v2.model.event_email_address_format import EventEmailAddressFormat
from datadog_api_client.v2.model.event_email_address_resource_type import EventEmailAddressResourceType
from datadog_api_client.v2.model.on_call_event_email_address_create_attributes import (
    OnCallEventEmailAddressCreateAttributes,
)
from datadog_api_client.v2.model.on_call_event_email_address_create_data import OnCallEventEmailAddressCreateData
from datadog_api_client.v2.model.on_call_event_email_address_create_request import OnCallEventEmailAddressCreateRequest

body = OnCallEventEmailAddressCreateRequest(
    data=OnCallEventEmailAddressCreateData(
        attributes=OnCallEventEmailAddressCreateAttributes(
            alert_type=EventEmailAddressAlertType.INFO,
            description="On-call email address for my team.",
            format=EventEmailAddressFormat.JSON,
            tags=[
                "env:production",
                "team:my-team",
            ],
            team_handle="my-team",
        ),
        type=EventEmailAddressResourceType.EVENT_EMAILS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_on_call_event_email_address"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_on_call_event_email_address(body=body)

    print(response)
