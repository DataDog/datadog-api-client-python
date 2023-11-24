"""
Update a user's membership attributes on a team returns "Represents a user's association to a team" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.user_team_attributes import UserTeamAttributes
from datadog_api_client.v2.model.user_team_type import UserTeamType
from datadog_api_client.v2.model.user_team_update import UserTeamUpdate
from datadog_api_client.v2.model.user_team_update_request import UserTeamUpdateRequest

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = UserTeamUpdateRequest(
    data=UserTeamUpdate(
        attributes=UserTeamAttributes(
            role=None,
        ),
        type=UserTeamType.TEAM_MEMBERSHIPS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team_membership(team_id=DD_TEAM_DATA_ID, user_id=USER_DATA_ID, body=body)

    print(response)
