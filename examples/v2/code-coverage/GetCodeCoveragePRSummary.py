"""
Get code coverage summary for a pull request returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.code_coverage_api import CodeCoverageApi
from datadog_api_client.v2.model.pr_coverage_summary_request import PRCoverageSummaryRequest
from datadog_api_client.v2.model.pr_coverage_summary_request_attributes import PRCoverageSummaryRequestAttributes
from datadog_api_client.v2.model.pr_coverage_summary_request_data import PRCoverageSummaryRequestData
from datadog_api_client.v2.model.pr_coverage_summary_request_type import PRCoverageSummaryRequestType

body = PRCoverageSummaryRequest(
    data=PRCoverageSummaryRequestData(
        attributes=PRCoverageSummaryRequestAttributes(
            pr_number=42,
            repository_url="https://github.com/datadog/shopist",
        ),
        type=PRCoverageSummaryRequestType.CI_APP_COVERAGE_PR_SUMMARY_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CodeCoverageApi(api_client)
    response = api_instance.get_code_coverage_pr_summary(body=body)

    print(response)
