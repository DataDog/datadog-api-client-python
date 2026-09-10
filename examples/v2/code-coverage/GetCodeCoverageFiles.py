"""
Get per-file code coverage data returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.code_coverage_api import CodeCoverageApi
from datadog_api_client.v2.model.files_coverage_request import FilesCoverageRequest
from datadog_api_client.v2.model.files_coverage_request_attributes import FilesCoverageRequestAttributes
from datadog_api_client.v2.model.files_coverage_request_data import FilesCoverageRequestData
from datadog_api_client.v2.model.files_coverage_request_type import FilesCoverageRequestType

body = FilesCoverageRequest(
    data=FilesCoverageRequestData(
        attributes=FilesCoverageRequestAttributes(
            changed_only=True,
            commit_sha="66adc9350f2cc9b250b69abddab733dd55e1a588",
            repository_url="https://github.com/datadog/shopist",
        ),
        type=FilesCoverageRequestType.CI_APP_COVERAGE_FILES_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CodeCoverageApi(api_client)
    response = api_instance.get_code_coverage_files(body=body)

    print(response)
