"""
Get an event email address returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_event_email_address"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.get_event_email_address(
        email_uuid=UUID("00000000-0000-0000-0000-000000000001"),
    )

    print(response)
