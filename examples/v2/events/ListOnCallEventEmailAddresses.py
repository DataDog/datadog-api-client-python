"""
List on-call event email addresses returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi

configuration = Configuration()
configuration.unstable_operations["list_on_call_event_email_addresses"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.list_on_call_event_email_addresses(
        filter_team_handle="my-team",
    )

    print(response)
