"""
Remove a team hierarchy link returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

# there is a valid "team_hierarchy_link" in the system
TEAM_HIERARCHY_LINK_DATA_ID = environ["TEAM_HIERARCHY_LINK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.remove_team_hierarchy_link(
        link_id=TEAM_HIERARCHY_LINK_DATA_ID,
    )
