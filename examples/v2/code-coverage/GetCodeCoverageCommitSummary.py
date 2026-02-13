"""
Get code coverage summary for a commit returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.code_coverage_api import CodeCoverageApi
from datadog_api_client.v2.model.commit_coverage_summary_request import CommitCoverageSummaryRequest
from datadog_api_client.v2.model.commit_coverage_summary_request_attributes import (
    CommitCoverageSummaryRequestAttributes,
)
from datadog_api_client.v2.model.commit_coverage_summary_request_data import CommitCoverageSummaryRequestData
from datadog_api_client.v2.model.commit_coverage_summary_request_type import CommitCoverageSummaryRequestType

body = CommitCoverageSummaryRequest(
    data=CommitCoverageSummaryRequestData(
        attributes=CommitCoverageSummaryRequestAttributes(
            commit_sha="66adc9350f2cc9b250b69abddab733dd55e1a588",
            repository_id="github.com/datadog/shopist",
        ),
        type=CommitCoverageSummaryRequestType.CI_APP_COVERAGE_COMMIT_SUMMARY_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_code_coverage_commit_summary"] = True
with ApiClient(configuration) as api_client:
    api_instance = CodeCoverageApi(api_client)
    response = api_instance.get_code_coverage_commit_summary(body=body)

    print(response)
