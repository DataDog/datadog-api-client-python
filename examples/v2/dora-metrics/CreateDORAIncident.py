"""
Send an incident event for DORA Metrics returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_git_info import DORAGitInfo
from datadog_api_client.v2.model.dora_incident_request import DORAIncidentRequest
from datadog_api_client.v2.model.dora_incident_request_attributes import DORAIncidentRequestAttributes
from datadog_api_client.v2.model.dora_incident_request_data import DORAIncidentRequestData

body = DORAIncidentRequest(
    data=DORAIncidentRequestData(
        attributes=DORAIncidentRequestAttributes(
            finished_at=1707842944600000000,
            git=DORAGitInfo(
                commit_sha="66adc9350f2cc9b250b69abddab733dd55e1a588",
                repository_url="https://github.com/organization/example-repository",
            ),
            name="Webserver is down failing all requests",
            services=[
                "shopist",
            ],
            severity="High",
            started_at=1707842944500000000,
            team="backend",
            version="v1.12.07",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_dora_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.create_dora_incident(body=body)

    print(response)
