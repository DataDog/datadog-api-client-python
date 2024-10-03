"""
Create tenant-based handle returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_create_tenant_based_handle_request import (
    MicrosoftTeamsCreateTenantBasedHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_request_attributes import (
    MicrosoftTeamsTenantBasedHandleRequestAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_request_data import (
    MicrosoftTeamsTenantBasedHandleRequestData,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_type import MicrosoftTeamsTenantBasedHandleType

body = MicrosoftTeamsCreateTenantBasedHandleRequest(
    data=MicrosoftTeamsTenantBasedHandleRequestData(
        attributes=MicrosoftTeamsTenantBasedHandleRequestAttributes(
            channel_id="fake-channel-id",
            name="fake-handle-name",
            team_id="00000000-0000-0000-0000-000000000000",
            tenant_id="00000000-0000-0000-0000-000000000001",
        ),
        type=MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.create_tenant_based_handle(body=body)

    print(response)
