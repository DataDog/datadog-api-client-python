"""
Get team hierarchy members paginates by number and size
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
        filter_keyword="Example-Team",
        sort="-is_direct",
        page_number=1,
        page_size=1,
    )

    print(response)
