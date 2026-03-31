"""
Add a user to a team returns "Represents a user's association to a team" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.relationship_to_user_team_user import RelationshipToUserTeamUser
from datadog_api_client.v2.model.relationship_to_user_team_user_data import RelationshipToUserTeamUserData
from datadog_api_client.v2.model.user_team_attributes import UserTeamAttributes
from datadog_api_client.v2.model.user_team_create import UserTeamCreate
from datadog_api_client.v2.model.user_team_relationships import UserTeamRelationships
from datadog_api_client.v2.model.user_team_request import UserTeamRequest
from datadog_api_client.v2.model.user_team_role import UserTeamRole
from datadog_api_client.v2.model.user_team_type import UserTeamType
from datadog_api_client.v2.model.user_team_user_type import UserTeamUserType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = UserTeamRequest(
    data=UserTeamCreate(
        attributes=UserTeamAttributes(
            role=UserTeamRole.ADMIN,
        ),
        relationships=UserTeamRelationships(
            user=RelationshipToUserTeamUser(
                data=RelationshipToUserTeamUserData(
                    id=USER_DATA_ID,
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
    response = api_instance.create_team_membership(team_id=DD_TEAM_DATA_ID, body=body)

    print(response)
