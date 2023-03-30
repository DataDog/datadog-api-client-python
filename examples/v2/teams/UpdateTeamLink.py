"""
Update a team link returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_link_attributes import TeamLinkAttributes
from datadog_api_client.v2.model.team_link_create import TeamLinkCreate
from datadog_api_client.v2.model.team_link_create_request import TeamLinkCreateRequest
from datadog_api_client.v2.model.team_link_type import TeamLinkType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

# there is a valid "team_link" in the system
TEAM_LINK_DATA_ID = environ["TEAM_LINK_DATA_ID"]

body = TeamLinkCreateRequest(
    data=TeamLinkCreate(
        attributes=TeamLinkAttributes(
            label="New Label",
            url="https://example.com",
        ),
        type=TeamLinkType.TEAM_LINKS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.update_team_link(team_id=DD_TEAM_DATA_ID, link_id=TEAM_LINK_DATA_ID, body=body)

    print(response)
