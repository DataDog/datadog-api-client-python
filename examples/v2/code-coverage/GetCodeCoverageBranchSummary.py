"""
Get code coverage summary for a branch returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.code_coverage_api import CodeCoverageApi
from datadog_api_client.v2.model.branch_coverage_summary_request import BranchCoverageSummaryRequest
from datadog_api_client.v2.model.branch_coverage_summary_request_attributes import (
    BranchCoverageSummaryRequestAttributes,
)
from datadog_api_client.v2.model.branch_coverage_summary_request_data import BranchCoverageSummaryRequestData
from datadog_api_client.v2.model.branch_coverage_summary_request_type import BranchCoverageSummaryRequestType

body = BranchCoverageSummaryRequest(
    data=BranchCoverageSummaryRequestData(
        attributes=BranchCoverageSummaryRequestAttributes(
            branch="prod",
            repository_id="github.com/datadog/shopist",
        ),
        type=BranchCoverageSummaryRequestType.CI_APP_COVERAGE_BRANCH_SUMMARY_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_code_coverage_branch_summary"] = True
with ApiClient(configuration) as api_client:
    api_instance = CodeCoverageApi(api_client)
    response = api_instance.get_code_coverage_branch_summary(body=body)

    print(response)
