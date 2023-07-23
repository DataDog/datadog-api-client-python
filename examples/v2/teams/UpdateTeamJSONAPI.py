"""
Update a team returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_update_request import TeamUpdateRequestJSON

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ATTRIBUTES_HANDLE = environ["DD_TEAM_DATA_ATTRIBUTES_HANDLE"]
DD_TEAM_DATA_ATTRIBUTES_NAME = environ["DD_TEAM_DATA_ATTRIBUTES_NAME"]
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamUpdateRequestJSON(
    handle=DD_TEAM_DATA_ATTRIBUTES_HANDLE,
    name="Example Team updated",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team(team_id=DD_TEAM_DATA_ID, body=body)

    print(response)
