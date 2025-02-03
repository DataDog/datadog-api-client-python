"""
Update workflow webhook handle returns "OK" response
"""

from os import environ
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

# there is a valid "workflows_webhook_handle" in the system
WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME = environ["WORKFLOWS_WEBHOOK_HANDLE_DATA_ATTRIBUTES_NAME"]
WORKFLOWS_WEBHOOK_HANDLE_DATA_ID = environ["WORKFLOWS_WEBHOOK_HANDLE_DATA_ID"]

body = MicrosoftTeamsUpdateWorkflowsWebhookHandleRequest(
    data=MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData(
        attributes=MicrosoftTeamsWorkflowsWebhookHandleAttributes(
            name="fake-handle-name--updated",
        ),
        type=MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.update_workflows_webhook_handle(handle_id=WORKFLOWS_WEBHOOK_HANDLE_DATA_ID, body=body)

    print(response)
