"""
Create a team link returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_link_create_request import TeamLinkCreateRequestJSON

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamLinkCreateRequestJSON(
    label="Link label",
    url="https://example.com",
    position=0,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team_link(team_id=DD_TEAM_DATA_ID, body=body)

    print(response)
