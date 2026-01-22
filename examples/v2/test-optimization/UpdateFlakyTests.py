"""
Update flaky test states returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.test_optimization_api import TestOptimizationApi
from datadog_api_client.v2.model.update_flaky_tests_request import UpdateFlakyTestsRequest
from datadog_api_client.v2.model.update_flaky_tests_request_attributes import UpdateFlakyTestsRequestAttributes
from datadog_api_client.v2.model.update_flaky_tests_request_data import UpdateFlakyTestsRequestData
from datadog_api_client.v2.model.update_flaky_tests_request_data_type import UpdateFlakyTestsRequestDataType
from datadog_api_client.v2.model.update_flaky_tests_request_test import UpdateFlakyTestsRequestTest
from datadog_api_client.v2.model.update_flaky_tests_request_test_new_state import UpdateFlakyTestsRequestTestNewState

body = UpdateFlakyTestsRequest(
    data=UpdateFlakyTestsRequestData(
        attributes=UpdateFlakyTestsRequestAttributes(
            tests=[
                UpdateFlakyTestsRequestTest(
                    id="4eb1887a8adb1847",
                    new_state=UpdateFlakyTestsRequestTestNewState.ACTIVE,
                ),
            ],
        ),
        type=UpdateFlakyTestsRequestDataType.UPDATE_FLAKY_TEST_STATE_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_flaky_tests"] = True
with ApiClient(configuration) as api_client:
    api_instance = TestOptimizationApi(api_client)
    response = api_instance.update_flaky_tests(body=body)

    print(response)
