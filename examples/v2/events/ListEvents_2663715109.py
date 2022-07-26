"""
Get a quick list of events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi

configuration = Configuration()
configuration.unstable_operations["list_events"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.list_events(
        filter_query="datadog-agent",
        filter_from="2020-09-17T11:48:36+01:00",
        filter_to="2020-09-17T12:48:36+01:00",
        page_limit=5,
    )

    print(response)
