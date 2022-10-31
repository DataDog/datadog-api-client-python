"""
Search tests events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_tests_api import CIVisibilityTestsApi
from datadog_api_client.v2.model.ci_app_query_page_options import CIAppQueryPageOptions
from datadog_api_client.v2.model.ci_app_sort import CIAppSort
from datadog_api_client.v2.model.ci_app_test_events_request import CIAppTestEventsRequest
from datadog_api_client.v2.model.ci_app_tests_query_filter import CIAppTestsQueryFilter

body = CIAppTestEventsRequest(
    filter=CIAppTestsQueryFilter(
        _from="now-15m",
        query="@test.status:pass AND -@language:python",
        to="now",
    ),
    page=CIAppQueryPageOptions(
        limit=2,
    ),
    sort=CIAppSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityTestsApi(api_client)
    items = api_instance.search_ci_app_test_events_with_pagination(body=body)
    for item in items:
        print(item)
