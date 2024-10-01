"""
Create handle returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_api_handle_request_attributes import (
    MicrosoftTeamsApiHandleRequestAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_api_handle_request_data import MicrosoftTeamsApiHandleRequestData
from datadog_api_client.v2.model.microsoft_teams_api_handle_type import MicrosoftTeamsApiHandleType
from datadog_api_client.v2.model.microsoft_teams_create_api_handle_request import MicrosoftTeamsCreateApiHandleRequest

body = MicrosoftTeamsCreateApiHandleRequest(
    data=MicrosoftTeamsApiHandleRequestData(
        attributes=MicrosoftTeamsApiHandleRequestAttributes(
            channel_id="fake-channel-id",
            name="fake-handle-name",
            team_id="00000000-0000-0000-0000-000000000000",
            tenant_id="00000000-0000-0000-0000-000000000001",
        ),
        type=MicrosoftTeamsApiHandleType.HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.create_api_handle(body=body)

    print(response)
