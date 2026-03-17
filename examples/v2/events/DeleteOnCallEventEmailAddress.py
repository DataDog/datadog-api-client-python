"""
Revoke an on-call event email address returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_on_call_event_email_address"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    api_instance.delete_on_call_event_email_address(
        id=UUID("00000000-0000-0000-0000-000000000001"),
    )
