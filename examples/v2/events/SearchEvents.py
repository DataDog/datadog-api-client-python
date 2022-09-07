"""
Search events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.events_list_request import EventsListRequest
from datadog_api_client.v2.model.events_query_filter import EventsQueryFilter
from datadog_api_client.v2.model.events_request_page import EventsRequestPage
from datadog_api_client.v2.model.events_sort import EventsSort

body = EventsListRequest(
    filter=EventsQueryFilter(
        query="datadog-agent",
        _from="2020-09-17T11:48:36+01:00",
        to="2020-09-17T12:48:36+01:00",
    ),
    sort=EventsSort.TIMESTAMP_ASCENDING,
    page=EventsRequestPage(
        limit=5,
    ),
)

configuration = Configuration()
configuration.unstable_operations["search_events"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.search_events(body=body)

    print(response)
