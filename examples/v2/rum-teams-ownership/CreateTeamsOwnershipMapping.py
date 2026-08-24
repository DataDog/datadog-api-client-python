"""
Create a teams ownership mapping returns "Created" response
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
from uuid import UUID

body = TeamsOwnershipMappingCreateRequest(
    data=TeamsOwnershipMappingCreateData(
        attributes=TeamsOwnershipMappingCreateDataAttributes(
            application_id=UUID("11111111-2222-3333-4444-555555555555"),
            match_type=TeamsOwnershipMatchType.EXACT,
            service="web-checkout",
            team_handle="team-rum",
            view_name="/checkout",
        ),
        type=TeamsOwnershipMappingType.TEAMS_OWNERSHIP_MAPPINGS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_teams_ownership_mapping"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumTeamsOwnershipApi(api_client)
    response = api_instance.create_teams_ownership_mapping(body=body)

    print(response)
