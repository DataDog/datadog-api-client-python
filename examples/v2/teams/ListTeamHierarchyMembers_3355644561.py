"""
Get team hierarchy members filters direct members
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_team_hierarchy_members"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.list_team_hierarchy_members(
        team_id=DD_TEAM_DATA_ID,
        filter_is_direct_only=True,
        filter_include_service_accounts=False,
        filter_keyword="Example-Team",
    )

    print(response)
