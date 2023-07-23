"""
Create a team returns "CREATED" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_create_request import TeamCreateRequestJSON

body = TeamCreateRequestJSON(
    handle="handle-a0fc0297eb519635",
    name="name-a0fc0297eb519635",
    users=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team(body=body)

    print(response)
