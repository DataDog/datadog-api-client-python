"""
Search flaky tests returns "OK" response with cursor pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.test_optimization_api import TestOptimizationApi
from datadog_api_client.v2.model.flaky_tests_search_filter import FlakyTestsSearchFilter
from datadog_api_client.v2.model.flaky_tests_search_page_options import FlakyTestsSearchPageOptions
from datadog_api_client.v2.model.flaky_tests_search_request import FlakyTestsSearchRequest
from datadog_api_client.v2.model.flaky_tests_search_request_attributes import FlakyTestsSearchRequestAttributes
from datadog_api_client.v2.model.flaky_tests_search_request_data import FlakyTestsSearchRequestData
from datadog_api_client.v2.model.flaky_tests_search_request_data_type import FlakyTestsSearchRequestDataType
from datadog_api_client.v2.model.flaky_tests_search_sort import FlakyTestsSearchSort

body = FlakyTestsSearchRequest(
    data=FlakyTestsSearchRequestData(
        attributes=FlakyTestsSearchRequestAttributes(
            filter=FlakyTestsSearchFilter(
                query="*",
            ),
            page=FlakyTestsSearchPageOptions(
                limit=2,
            ),
            sort=FlakyTestsSearchSort.FQN_ASCENDING,
        ),
        type=FlakyTestsSearchRequestDataType.SEARCH_FLAKY_TESTS_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TestOptimizationApi(api_client)
    items = api_instance.search_flaky_tests_with_pagination(body=body)
    for item in items:
        print(item)
