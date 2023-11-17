"""
Send a deployment event for DORA Metrics returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_deployment_request import DORADeploymentRequest
from datadog_api_client.v2.model.dora_deployment_request_attributes import DORADeploymentRequestAttributes
from datadog_api_client.v2.model.dora_deployment_request_data import DORADeploymentRequestData
from datadog_api_client.v2.model.dora_git_info import DORAGitInfo

body = DORADeploymentRequest(
    data=DORADeploymentRequestData(
        attributes=DORADeploymentRequestAttributes(
            finished_at=1693491984000000000,
            git=DORAGitInfo(
                commit_sha="66adc9350f2cc9b250b69abddab733dd55e1a588",
                repository_url="https://github.com/organization/example-repository",
            ),
            service="shopist",
            started_at=1693491974000000000,
            version="v1.12.07",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_dora_deployment"] = True
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.create_dora_deployment(body=body)

    print(response)
