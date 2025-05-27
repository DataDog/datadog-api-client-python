"""
Remove a member team returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
configuration.unstable_operations["remove_member_team"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.remove_member_team(
        super_team_id="super_team_id",
        member_team_id="member_team_id",
    )
