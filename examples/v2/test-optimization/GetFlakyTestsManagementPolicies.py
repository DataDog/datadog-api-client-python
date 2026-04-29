"""
Get Flaky Tests Management policies returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.test_optimization_api import TestOptimizationApi
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_get_request import (
    TestOptimizationFlakyTestsManagementPoliciesGetRequest,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_get_request_attributes import (
    TestOptimizationFlakyTestsManagementPoliciesGetRequestAttributes,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_get_request_data import (
    TestOptimizationFlakyTestsManagementPoliciesGetRequestData,
)
from datadog_api_client.v2.model.test_optimization_get_flaky_tests_management_policies_request_data_type import (
    TestOptimizationGetFlakyTestsManagementPoliciesRequestDataType,
)

body = TestOptimizationFlakyTestsManagementPoliciesGetRequest(
    data=TestOptimizationFlakyTestsManagementPoliciesGetRequestData(
        attributes=TestOptimizationFlakyTestsManagementPoliciesGetRequestAttributes(
            repository_id="github.com/datadog/shopist",
        ),
        type=TestOptimizationGetFlakyTestsManagementPoliciesRequestDataType.TEST_OPTIMIZATION_GET_FLAKY_TESTS_MANAGEMENT_POLICIES_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TestOptimizationApi(api_client)
    response = api_instance.get_flaky_tests_management_policies(body=body)

    print(response)
