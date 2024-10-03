"""
Update api handle returns "OK" response
"""

from os import environ
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

# there is a valid "tenant_based_handle" in the system
TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME = environ["TENANT_BASED_HANDLE_DATA_ATTRIBUTES_NAME"]
TENANT_BASED_HANDLE_DATA_ID = environ["TENANT_BASED_HANDLE_DATA_ID"]

body = MicrosoftTeamsUpdateTenantBasedHandleRequest(
    data=MicrosoftTeamsUpdateTenantBasedHandleRequestData(
        attributes=MicrosoftTeamsTenantBasedHandleAttributes(
            name="fake-handle-name--updated",
        ),
        type=MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.update_tenant_based_handle(handle_id=TENANT_BASED_HANDLE_DATA_ID, body=body)

    print(response)
