"""
Add a member team returns "Added" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.add_member_team_request import AddMemberTeamRequest
from datadog_api_client.v2.model.member_team import MemberTeam
from datadog_api_client.v2.model.member_team_type import MemberTeamType

body = AddMemberTeamRequest(
    data=MemberTeam(
        id="aeadc05e-98a8-11ec-ac2c-da7ad0900001",
        type=MemberTeamType.MEMBER_TEAMS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["add_member_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.add_member_team(super_team_id="super_team_id", body=body)
