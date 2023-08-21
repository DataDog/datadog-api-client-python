"""
Update a team returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_type import TeamType
from datadog_api_client.v2.model.team_update import TeamUpdate
from datadog_api_client.v2.model.team_update_attributes import TeamUpdateAttributes
from datadog_api_client.v2.model.team_update_request import TeamUpdateRequest

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ATTRIBUTES_HANDLE = environ["DD_TEAM_DATA_ATTRIBUTES_HANDLE"]
DD_TEAM_DATA_ATTRIBUTES_NAME = environ["DD_TEAM_DATA_ATTRIBUTES_NAME"]
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamUpdateRequest(
    data=TeamUpdate(
        attributes=TeamUpdateAttributes(
            handle=DD_TEAM_DATA_ATTRIBUTES_HANDLE,
            name="Example Team updated",
            avatar="🥑",
            banner=7,
            hidden_modules=[
                "m3",
            ],
            visible_modules=[
                "m1",
                "m2",
            ],
        ),
        type=TeamType.TEAM,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team(team_id=DD_TEAM_DATA_ID, body=body)

    print(response)
