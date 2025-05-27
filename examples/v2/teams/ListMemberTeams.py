"""
Get all member teams returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
configuration.unstable_operations["list_member_teams"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.list_member_teams(
        super_team_id="super_team_id",
    )

    print(response)
