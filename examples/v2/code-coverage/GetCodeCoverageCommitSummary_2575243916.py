"""
Get code coverage summary for an existing commit with valid repository
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
            repository_id="github.com/datadog/shopist",
            commit_sha="c55b0ce584e139bde41a00002ab31bc7d75f791d",
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
