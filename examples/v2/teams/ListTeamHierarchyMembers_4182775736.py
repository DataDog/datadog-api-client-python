"""
Get team hierarchy members returns "OK" response with pagination
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
    items = api_instance.list_team_hierarchy_members_with_pagination(
        team_id=DD_TEAM_DATA_ID,
        filter_keyword="Example-Team",
        page_size=1,
    )
    for item in items:
        print(item)
