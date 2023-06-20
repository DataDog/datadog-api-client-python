"""
Add a user to a team returns "Represents a user's association to a team" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.user_team_request import UserTeamRequestJSON
from datadog_api_client.v2.model.user_team_role import UserTeamRole

body = UserTeamRequestJSON(
    role=UserTeamRole.ADMIN,
    user="b8626d7e-cedd-11eb-abf5-da7ad0900001",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team_membership(team_id="team_id", body=body)

    print(response)
