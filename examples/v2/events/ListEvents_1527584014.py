"""
Get a list of events returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    items = api_instance.list_events_with_pagination(
        filter_from="now-15m",
        filter_to="now",
        page_limit=2,
    )
    for item in items:
        print(item)
