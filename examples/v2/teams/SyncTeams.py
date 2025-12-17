"""
Link Teams with GitHub Teams returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi
from datadog_api_client.v2.model.team_sync_attributes import TeamSyncAttributes
from datadog_api_client.v2.model.team_sync_attributes_source import TeamSyncAttributesSource
from datadog_api_client.v2.model.team_sync_attributes_type import TeamSyncAttributesType
from datadog_api_client.v2.model.team_sync_bulk_type import TeamSyncBulkType
from datadog_api_client.v2.model.team_sync_data import TeamSyncData
from datadog_api_client.v2.model.team_sync_request import TeamSyncRequest

body = TeamSyncRequest(
    data=TeamSyncData(
        attributes=TeamSyncAttributes(
            source=TeamSyncAttributesSource.GITHUB,
            type=TeamSyncAttributesType.LINK,
        ),
        type=TeamSyncBulkType.TEAM_SYNC_BULK,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    api_instance.sync_teams(body=body)
