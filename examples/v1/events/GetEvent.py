"""
Get an event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.events_api import EventsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.get_event(
        event_id=9223372036854775807,
    )

    print(response)
