"""
Search tests events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_tests_api import CIVisibilityTestsApi
from datadog_api_client.v2.model.ci_app_query_options import CIAppQueryOptions
from datadog_api_client.v2.model.ci_app_query_page_options import CIAppQueryPageOptions
from datadog_api_client.v2.model.ci_app_sort import CIAppSort
from datadog_api_client.v2.model.ci_app_test_events_request import CIAppTestEventsRequest
from datadog_api_client.v2.model.ci_app_tests_query_filter import CIAppTestsQueryFilter

body = CIAppTestEventsRequest(
    filter=CIAppTestsQueryFilter(
        _from="now-15m",
        query="@test.service:web-ui-tests AND @test.status:skip",
        to="now",
    ),
    options=CIAppQueryOptions(
        timezone="GMT",
    ),
    page=CIAppQueryPageOptions(
        limit=25,
    ),
    sort=CIAppSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityTestsApi(api_client)
    response = api_instance.search_ci_app_test_events(body=body)

    print(response)
