"""
Get all member teams returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
configuration.unstable_operations["list_member_teams"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    items = api_instance.list_member_teams_with_pagination(
        super_team_id="super_team_id",
    )
    for item in items:
        print(item)
