"""
List team connections with filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.teams_api import TeamsApi

configuration = Configuration()
configuration.unstable_operations["list_team_connections"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamsApi(api_client)
    response = api_instance.list_team_connections(
        page_size=10,
        filter_sources=[
            "github",
        ],
    )

    print(response)
