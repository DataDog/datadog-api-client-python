"""
Update tenant-based handle returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_attributes import (
    MicrosoftTeamsTenantBasedHandleAttributes,
)
from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_type import MicrosoftTeamsTenantBasedHandleType
from datadog_api_client.v2.model.microsoft_teams_update_tenant_based_handle_request import (
    MicrosoftTeamsUpdateTenantBasedHandleRequest,
)
from datadog_api_client.v2.model.microsoft_teams_update_tenant_based_handle_request_data import (
    MicrosoftTeamsUpdateTenantBasedHandleRequestData,
)

body = MicrosoftTeamsUpdateTenantBasedHandleRequest(
    data=MicrosoftTeamsUpdateTenantBasedHandleRequestData(
        attributes=MicrosoftTeamsTenantBasedHandleAttributes(
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
    response = api_instance.update_tenant_based_handle(handle_id="handle_id", body=body)

    print(response)
