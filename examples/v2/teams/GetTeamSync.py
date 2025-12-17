"""
Get team sync configurations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_sync_attributes_source import TeamSyncAttributesSource

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.get_team_sync(
        filter_source=TeamSyncAttributesSource.GITHUB,
    )

    print(response)
