"""
Add a user to a team returns "Represents a user's association to a team" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.relationship_to_user_team_team import RelationshipToUserTeamTeam
from datadog_api_client.v2.model.relationship_to_user_team_team_data import RelationshipToUserTeamTeamData
from datadog_api_client.v2.model.relationship_to_user_team_user import RelationshipToUserTeamUser
from datadog_api_client.v2.model.relationship_to_user_team_user_data import RelationshipToUserTeamUserData
from datadog_api_client.v2.model.user_team_attributes import UserTeamAttributes
from datadog_api_client.v2.model.user_team_create import UserTeamCreate
from datadog_api_client.v2.model.user_team_relationships import UserTeamRelationships
from datadog_api_client.v2.model.user_team_request import UserTeamRequest
from datadog_api_client.v2.model.user_team_role import UserTeamRole
from datadog_api_client.v2.model.user_team_team_type import UserTeamTeamType
from datadog_api_client.v2.model.user_team_type import UserTeamType
from datadog_api_client.v2.model.user_team_user_type import UserTeamUserType

body = UserTeamRequest(
    data=UserTeamCreate(
        attributes=UserTeamAttributes(
            role=UserTeamRole.ADMIN,
        ),
        relationships=UserTeamRelationships(
            team=RelationshipToUserTeamTeam(
                data=RelationshipToUserTeamTeamData(
                    id="d7e15d9d-d346-43da-81d8-3d9e71d9a5e9",
                    type=UserTeamTeamType.TEAM,
                ),
            ),
            user=RelationshipToUserTeamUser(
                data=RelationshipToUserTeamUserData(
                    id="b8626d7e-cedd-11eb-abf5-da7ad0900001",
                    type=UserTeamUserType.USERS,
                ),
            ),
        ),
        type=UserTeamType.TEAM_MEMBERSHIPS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team_membership(team_id="team_id", body=body)

    print(response)
