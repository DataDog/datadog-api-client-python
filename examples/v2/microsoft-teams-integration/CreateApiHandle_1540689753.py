"""
Create api handle returns "CREATED" response
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
            channel_id="19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2",
            name="Example-Microsoft-Teams-Integration",
            team_id="e5f50a58-c929-4fb3-8866-e2cd836de3c2",
            tenant_id="4d3bac44-0230-4732-9e70-cc00736f0a97",
        ),
        type=MicrosoftTeamsApiHandleType.HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.create_api_handle(body=body)

    print(response)
