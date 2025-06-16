"""
Create workflow webhook handle returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_create_workflows_webhook_handle_request import (
    MicrosoftTeamsCreateWorkflowsWebhookHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_request_attributes import (
    MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_request_data import (
    MicrosoftTeamsWorkflowsWebhookHandleRequestData,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_type import (
    MicrosoftTeamsWorkflowsWebhookHandleType,
)

body = MicrosoftTeamsCreateWorkflowsWebhookHandleRequest(
    data=MicrosoftTeamsWorkflowsWebhookHandleRequestData(
        attributes=MicrosoftTeamsWorkflowsWebhookHandleRequestAttributes(
            name="Example-Microsoft-Teams-Integration",
            url="https://example.logic.azure.com/workflows/123",
        ),
        type=MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.create_workflows_webhook_handle(body=body)

    print(response)
