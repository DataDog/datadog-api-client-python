"""
Create team connections returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.connected_team_ref import ConnectedTeamRef
from datadog_api_client.v2.model.connected_team_ref_data import ConnectedTeamRefData
from datadog_api_client.v2.model.connected_team_ref_data_type import ConnectedTeamRefDataType
from datadog_api_client.v2.model.team_connection_attributes import TeamConnectionAttributes
from datadog_api_client.v2.model.team_connection_create_data import TeamConnectionCreateData
from datadog_api_client.v2.model.team_connection_create_request import TeamConnectionCreateRequest
from datadog_api_client.v2.model.team_connection_relationships import TeamConnectionRelationships
from datadog_api_client.v2.model.team_connection_type import TeamConnectionType
from datadog_api_client.v2.model.team_ref import TeamRef
from datadog_api_client.v2.model.team_ref_data import TeamRefData
from datadog_api_client.v2.model.team_ref_data_type import TeamRefDataType

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = TeamConnectionCreateRequest(
    data=[
        TeamConnectionCreateData(
            type=TeamConnectionType.TEAM_CONNECTION,
            attributes=TeamConnectionAttributes(
                source="github",
                managed_by="datadog",
            ),
            relationships=TeamConnectionRelationships(
                team=TeamRef(
                    data=TeamRefData(
                        id=DD_TEAM_DATA_ID,
                        type=TeamRefDataType.TEAM,
                    ),
                ),
                connected_team=ConnectedTeamRef(
                    data=ConnectedTeamRefData(
                        id="@MyGitHubAccount/my-team-name",
                        type=ConnectedTeamRefDataType.GITHUB_TEAM,
                    ),
                ),
            ),
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["create_team_connections"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.create_team_connections(body=body)

    print(response)
