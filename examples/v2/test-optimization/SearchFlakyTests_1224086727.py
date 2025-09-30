"""
Search flaky tests returns "OK" response with pagination
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
                query='flaky_test_state:active @git.repository.id_v2:"github.com/datadog/shopist"',
            ),
            page=FlakyTestsSearchPageOptions(
                cursor="eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
                limit=25,
            ),
            sort=FlakyTestsSearchSort.FAILURE_RATE_ASCENDING,
        ),
        type=FlakyTestsSearchRequestDataType.SEARCH_FLAKY_TESTS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["search_flaky_tests"] = True
with ApiClient(configuration) as api_client:
    api_instance = TestOptimizationApi(api_client)
    items = api_instance.search_flaky_tests_with_pagination(body=body)
    for item in items:
        print(item)
