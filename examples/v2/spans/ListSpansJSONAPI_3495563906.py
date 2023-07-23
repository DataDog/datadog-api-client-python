"""
Search spans returns "OK" response with pagination using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_api import SpansApi
from datadog_api_client.v2.model.spans_list_request import SpansListRequestJSON
from datadog_api_client.v2.model.spans_list_request_page import SpansListRequestPage
from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter
from datadog_api_client.v2.model.spans_query_options import SpansQueryOptions
from datadog_api_client.v2.model.spans_sort import SpansSort

body = SpansListRequestJSON(
    filter=SpansQueryFilter(
        _from="now-15m",
        query="service:python*",
        to="now",
    ),
    options=SpansQueryOptions(
        timezone="GMT",
    ),
    page=SpansListRequestPage(
        limit=2,
    ),
    sort=SpansSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansApi(api_client)
    items = api_instance.list_spans_with_pagination(body=body)
    for item in items:
        print(item)
