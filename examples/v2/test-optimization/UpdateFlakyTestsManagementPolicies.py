"""
Update Flaky Tests Management policies returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.test_optimization_api import TestOptimizationApi
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_attempt_to_fix import (
    TestOptimizationFlakyTestsManagementPoliciesAttemptToFix,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_auto_disable_rule import (
    TestOptimizationFlakyTestsManagementPoliciesAutoDisableRule,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_auto_quarantine_rule import (
    TestOptimizationFlakyTestsManagementPoliciesAutoQuarantineRule,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_branch_rule import (
    TestOptimizationFlakyTestsManagementPoliciesBranchRule,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_disabled import (
    TestOptimizationFlakyTestsManagementPoliciesDisabled,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_disabled_failure_rate_rule import (
    TestOptimizationFlakyTestsManagementPoliciesDisabledFailureRateRule,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_disabled_status import (
    TestOptimizationFlakyTestsManagementPoliciesDisabledStatus,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_quarantined import (
    TestOptimizationFlakyTestsManagementPoliciesQuarantined,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_quarantined_failure_rate_rule import (
    TestOptimizationFlakyTestsManagementPoliciesQuarantinedFailureRateRule,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_update_request import (
    TestOptimizationFlakyTestsManagementPoliciesUpdateRequest,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_update_request_attributes import (
    TestOptimizationFlakyTestsManagementPoliciesUpdateRequestAttributes,
)
from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_update_request_data import (
    TestOptimizationFlakyTestsManagementPoliciesUpdateRequestData,
)
from datadog_api_client.v2.model.test_optimization_update_flaky_tests_management_policies_request_data_type import (
    TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType,
)

body = TestOptimizationFlakyTestsManagementPoliciesUpdateRequest(
    data=TestOptimizationFlakyTestsManagementPoliciesUpdateRequestData(
        attributes=TestOptimizationFlakyTestsManagementPoliciesUpdateRequestAttributes(
            attempt_to_fix=TestOptimizationFlakyTestsManagementPoliciesAttemptToFix(
                retries=3,
            ),
            disabled=TestOptimizationFlakyTestsManagementPoliciesDisabled(
                auto_disable_rule=TestOptimizationFlakyTestsManagementPoliciesAutoDisableRule(
                    enabled=False,
                    status=TestOptimizationFlakyTestsManagementPoliciesDisabledStatus.ACTIVE,
                    window_seconds=3600,
                ),
                branch_rule=TestOptimizationFlakyTestsManagementPoliciesBranchRule(
                    branches=[
                        "main",
                    ],
                    enabled=True,
                    excluded_branches=[],
                    excluded_test_services=[],
                ),
                enabled=False,
                failure_rate_rule=TestOptimizationFlakyTestsManagementPoliciesDisabledFailureRateRule(
                    branches=[],
                    enabled=False,
                    min_runs=10,
                    status=TestOptimizationFlakyTestsManagementPoliciesDisabledStatus.ACTIVE,
                    threshold=0.5,
                ),
            ),
            quarantined=TestOptimizationFlakyTestsManagementPoliciesQuarantined(
                auto_quarantine_rule=TestOptimizationFlakyTestsManagementPoliciesAutoQuarantineRule(
                    enabled=True,
                    window_seconds=3600,
                ),
                branch_rule=TestOptimizationFlakyTestsManagementPoliciesBranchRule(
                    branches=[
                        "main",
                    ],
                    enabled=True,
                    excluded_branches=[],
                    excluded_test_services=[],
                ),
                enabled=True,
                failure_rate_rule=TestOptimizationFlakyTestsManagementPoliciesQuarantinedFailureRateRule(
                    branches=[
                        "main",
                    ],
                    enabled=True,
                    min_runs=10,
                    threshold=0.5,
                ),
            ),
            repository_id="github.com/datadog/shopist",
        ),
        type=TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType.TEST_OPTIMIZATION_UPDATE_FLAKY_TESTS_MANAGEMENT_POLICIES_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TestOptimizationApi(api_client)
    response = api_instance.update_flaky_tests_management_policies(body=body)

    print(response)
