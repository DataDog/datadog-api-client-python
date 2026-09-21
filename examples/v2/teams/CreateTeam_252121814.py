"""
Create a team with V2 fields returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_create import TeamCreate
from datadog_api_client.v2.model.team_create_attributes import TeamCreateAttributes
from datadog_api_client.v2.model.team_create_request import TeamCreateRequest
from datadog_api_client.v2.model.team_type import TeamType

body = TeamCreateRequest(
    data=TeamCreate(
        attributes=TeamCreateAttributes(
            handle="test-handle-a0fc0297eb519635",
            name="test-name-a0fc0297eb519635",
            avatar="🥑",
            banner=7,
            visible_modules=[
                "m1",
                "m2",
            ],
            hidden_modules=[
                "m3",
            ],
        ),
        type=TeamType.TEAM,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team(body=body)

    print(response)
