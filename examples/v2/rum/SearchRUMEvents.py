"""
Search RUM events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_query_filter import RUMQueryFilter
from datadog_api_client.v2.model.rum_query_options import RUMQueryOptions
from datadog_api_client.v2.model.rum_query_page_options import RUMQueryPageOptions
from datadog_api_client.v2.model.rum_search_events_request import RUMSearchEventsRequest
from datadog_api_client.v2.model.rum_sort import RUMSort

body = RUMSearchEventsRequest(
    filter=RUMQueryFilter(
        _from="now-15m",
        query="@type:session AND @session.type:user",
        to="now",
    ),
    options=RUMQueryOptions(
        time_offset=0,
        timezone="GMT",
    ),
    page=RUMQueryPageOptions(
        limit=25,
    ),
    sort=RUMSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.search_rum_events(body=body)

    print(response)
