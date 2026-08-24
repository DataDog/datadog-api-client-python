"""
Create teams ownership mapping returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_teams_ownership_api import RumTeamsOwnershipApi
from datadog_api_client.v2.model.teams_ownership_mapping_create_data import TeamsOwnershipMappingCreateData
from datadog_api_client.v2.model.teams_ownership_mapping_create_data_attributes import (
    TeamsOwnershipMappingCreateDataAttributes,
)
from datadog_api_client.v2.model.teams_ownership_mapping_create_request import TeamsOwnershipMappingCreateRequest
from datadog_api_client.v2.model.teams_ownership_mapping_type import TeamsOwnershipMappingType
from datadog_api_client.v2.model.teams_ownership_match_type import TeamsOwnershipMatchType

body = TeamsOwnershipMappingCreateRequest(
    data=TeamsOwnershipMappingCreateData(
        type=TeamsOwnershipMappingType.TEAMS_OWNERSHIP_MAPPINGS,
        attributes=TeamsOwnershipMappingCreateDataAttributes(
            team_handle="team-rum",
            view_name="/checkout-examplerumteamsownership",
            service="web-checkout-examplerumteamsownership",
            match_type=TeamsOwnershipMatchType.EXACT,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumTeamsOwnershipApi(api_client)
    response = api_instance.create_teams_ownership_mapping(body=body)

    print(response)
