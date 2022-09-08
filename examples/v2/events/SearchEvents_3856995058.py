"""
Search events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.events_list_request import EventsListRequest
from datadog_api_client.v2.model.events_query_filter import EventsQueryFilter
from datadog_api_client.v2.model.events_query_options import EventsQueryOptions
from datadog_api_client.v2.model.events_request_page import EventsRequestPage
from datadog_api_client.v2.model.events_sort import EventsSort

body = EventsListRequest(
    filter=EventsQueryFilter(
        _from="now-15m",
        to="now",
    ),
    options=EventsQueryOptions(
        timezone="GMT",
    ),
    page=EventsRequestPage(
        limit=2,
    ),
    sort=EventsSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
configuration.unstable_operations["search_events"] = True
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    items = api_instance.search_events_with_pagination(body=body)
    for item in items:
        print(item)
