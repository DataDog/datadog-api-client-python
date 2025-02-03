"""
Update Workflows webhook handle returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_update_workflows_webhook_handle_request import (
    MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_update_workflows_webhook_handle_request_data import (
    MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_attributes import (
    MicrosoftTeamsWorkflowsWebhookHandleAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_type import (
    MicrosoftTeamsWorkflowsWebhookHandleType,
)

body = MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest(
    data=MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData(
        attributes=MicrosoftTeamsWorkflowsWebhookHandleAttributes(
            name="fake-handle-name",
            url="https://fake.url.com",
        ),
        type=MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.update_workflows_webhook_handle(handle_id="handle_id", body=body)

    print(response)
