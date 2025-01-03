"""
Search logs (POST) returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_list_request import LogsListRequest
from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
from datadog_api_client.v2.model.logs_query_options import LogsQueryOptions
from datadog_api_client.v2.model.logs_sort import LogsSort
from datadog_api_client.v2.model.logs_storage_tier import LogsStorageTier

body = LogsListRequest(
    filter=LogsQueryFilter(
        _from="now-15m",
        indexes=[
            "main",
            "web",
        ],
        query="service:web* AND @http.status_code:[200 TO 299]",
        storage_tier=LogsStorageTier.INDEXES,
        to="now",
    ),
    options=LogsQueryOptions(
        timezone="GMT",
    ),
    page=LogsListRequestPage(
        cursor="eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
        limit=25,
    ),
    sort=LogsSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    items = api_instance.list_logs_with_pagination(body=body)
    for item in items:
        print(item)
