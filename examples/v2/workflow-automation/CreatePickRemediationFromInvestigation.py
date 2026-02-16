"""
Pick remediation actions from investigation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.client_type import ClientType
from datadog_api_client.v2.model.pick_remediation_from_investigation_request import (
    PickRemediationFromInvestigationRequest,
)
from datadog_api_client.v2.model.stability_level import StabilityLevel

body = PickRemediationFromInvestigationRequest(
    client=ClientType.WORKFLOWS,
    integrations=[
        "aws",
        "datadog",
    ],
    investigation="High CPU usage detected on prod-server-01",
    number_of_keyword_variants=2,
    number_of_relevant_actions=5,
    stability=StabilityLevel.STABLE,
)

configuration = Configuration()
configuration.unstable_operations["create_pick_remediation_from_investigation"] = True
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.create_pick_remediation_from_investigation(body=body)

    print(response)
