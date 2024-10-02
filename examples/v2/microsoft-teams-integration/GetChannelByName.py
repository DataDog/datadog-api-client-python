"""
Get channel information by name returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.microsoft_teams_integration_api import MicrosoftTeamsIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MicrosoftTeamsIntegrationApi(api_client)
    response = api_instance.get_channel_by_name(
        tenant_name="tenant_name",
        team_name="team_name",
        channel_name="channel_name",
    )

    print(response)
