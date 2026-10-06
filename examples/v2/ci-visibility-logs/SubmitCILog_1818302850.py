"""
Send one CI job log returns "Request accepted for processing" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_logs_api import CIVisibilityLogsApi
from datadog_api_client.v2.model.ci_log_item import CILogItem

body = [
    CILogItem(
        message="Running go test ./...",
        pipeline_unique_id="3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
        job_id="job-456",
        provider_name="example-provider",
        line_number=1,
        status="warn",
        section_name="tests",
        ddtags="runner:linux,architecture:amd64",
    ),
]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityLogsApi(api_client)
    response = api_instance.submit_ci_log(body=body)

    print(response)
