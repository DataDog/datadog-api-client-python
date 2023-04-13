"""
Update a user's membership attributes on a team returns "Represents a user's association to a team" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.user_team_attributes import UserTeamAttributes
from datadog_api_client.v2.model.user_team_role import UserTeamRole
from datadog_api_client.v2.model.user_team_type import UserTeamType
from datadog_api_client.v2.model.user_team_update import UserTeamUpdate
from datadog_api_client.v2.model.user_team_update_request import UserTeamUpdateRequest

body = UserTeamUpdateRequest(
    data=UserTeamUpdate(
        attributes=UserTeamAttributes(
            role=UserTeamRole.ADMIN,
        ),
        type=UserTeamType.TEAM_MEMBERSHIPS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team_membership(team_id="team_id", user_id="user_id", body=body)

    print(response)
