"""
Update a user's membership attributes on a team returns "Represents a user's association to a team" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.user_team_role import UserTeamRole
from datadog_api_client.v2.model.user_team_update_request import UserTeamUpdateRequestJSON

body = UserTeamUpdateRequestJSON(
    role=UserTeamRole.ADMIN,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team_membership(team_id="team_id", user_id="user_id", body=body)

    print(response)
