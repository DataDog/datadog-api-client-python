"""
Update handle returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_api_handle_attributes import MicrosoftTeamsApiHandleAttributes
from datadog_api_client.v2.model.microsoft_teams_api_handle_type import MicrosoftTeamsApiHandleType
from datadog_api_client.v2.model.microsoft_teams_update_api_handle_request import MicrosoftTeamsUpdateApiHandleRequest
from datadog_api_client.v2.model.microsoft_teams_update_api_handle_request_data import (
    MicrosoftTeamsUpdateApiHandleRequestData,
)

body = MicrosoftTeamsUpdateApiHandleRequest(
    data=MicrosoftTeamsUpdateApiHandleRequestData(
        attributes=MicrosoftTeamsApiHandleAttributes(
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
    response = api_instance.update_api_handle(handle_id="handle_id", body=body)

    print(response)
