"""
Delete team connections returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_connection_delete_request import TeamConnectionDeleteRequest
from datadog_api_client.v2.model.team_connection_delete_request_data_item import TeamConnectionDeleteRequestDataItem
from datadog_api_client.v2.model.team_connection_type import TeamConnectionType

# there is a valid "team_connection" in the system
TEAM_CONNECTION_ID = environ["TEAM_CONNECTION_ID"]

body = TeamConnectionDeleteRequest(
    data=[
        TeamConnectionDeleteRequestDataItem(
            id=TEAM_CONNECTION_ID,
            type=TeamConnectionType.TEAM_CONNECTION,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.delete_team_connections(body=body)
