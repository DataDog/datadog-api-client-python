"""
Get all teams with fields_team parameter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.teams_field import TeamsField

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.list_teams(
        fields_team=[
            TeamsField.ID,
            TeamsField.NAME,
            TeamsField.HANDLE,
        ],
    )

    print(response)
