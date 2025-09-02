"""
Send an incident event for DORA Metrics returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_failure_request import DORAFailureRequest
from datadog_api_client.v2.model.dora_failure_request_attributes import DORAFailureRequestAttributes
from datadog_api_client.v2.model.dora_failure_request_data import DORAFailureRequestData
from datadog_api_client.v2.model.dora_git_info import DORAGitInfo

body = DORAFailureRequest(
    data=DORAFailureRequestData(
        attributes=DORAFailureRequestAttributes(
            custom_tags=[
                "language:java",
                "department:engineering",
            ],
            env="staging",
            finished_at=1693491984000000000,
            git=DORAGitInfo(
                commit_sha="66adc9350f2cc9b250b69abddab733dd55e1a588",
                repository_url="https://github.com/organization/example-repository",
            ),
            name="Webserver is down failing all requests.",
            services=[
                "shopist",
            ],
            severity="High",
            started_at=1693491974000000000,
            team="backend",
            version="v1.12.07",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.create_dora_incident(body=body)

    print(response)
