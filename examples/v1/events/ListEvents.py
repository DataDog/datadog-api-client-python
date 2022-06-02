"""
Query the event stream returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.events_api import EventsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.list_events(
        start=9223372036854775807,
        end=9223372036854775807,
    )

    print(response)
