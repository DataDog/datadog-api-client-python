"""
Create a team hierarchy link returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_hierarchy_link_create import TeamHierarchyLinkCreate
from datadog_api_client.v2.model.team_hierarchy_link_create_relationships import TeamHierarchyLinkCreateRelationships
from datadog_api_client.v2.model.team_hierarchy_link_create_request import TeamHierarchyLinkCreateRequest
from datadog_api_client.v2.model.team_hierarchy_link_create_team import TeamHierarchyLinkCreateTeam
from datadog_api_client.v2.model.team_hierarchy_link_create_team_relationship import (
    TeamHierarchyLinkCreateTeamRelationship,
)
from datadog_api_client.v2.model.team_hierarchy_link_type import TeamHierarchyLinkType
from datadog_api_client.v2.model.team_type import TeamType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "dd_team_2" in the system
DD_TEAM_2_DATA_ID = environ["DD_TEAM_2_DATA_ID"]

body = TeamHierarchyLinkCreateRequest(
    data=TeamHierarchyLinkCreate(
        relationships=TeamHierarchyLinkCreateRelationships(
            parent_team=TeamHierarchyLinkCreateTeamRelationship(
                data=TeamHierarchyLinkCreateTeam(
                    id=DD_TEAM_DATA_ID,
                    type=TeamType.TEAM,
                ),
            ),
            sub_team=TeamHierarchyLinkCreateTeamRelationship(
                data=TeamHierarchyLinkCreateTeam(
                    id=DD_TEAM_2_DATA_ID,
                    type=TeamType.TEAM,
                ),
            ),
        ),
        type=TeamHierarchyLinkType.TEAM_HIERARCHY_LINKS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.add_team_hierarchy_link(body=body)

    print(response)
