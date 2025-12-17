"""
Delete team connections returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_connection_delete_request import TeamConnectionDeleteRequest
from datadog_api_client.v2.model.team_connection_delete_request_data_item import TeamConnectionDeleteRequestDataItem
from datadog_api_client.v2.model.team_connection_type import TeamConnectionType

body = TeamConnectionDeleteRequest(
    data=[
        TeamConnectionDeleteRequestDataItem(
            id="12345678-1234-5678-9abc-123456789012",
            type=TeamConnectionType.TEAM_CONNECTION,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.delete_team_connections(body=body)
