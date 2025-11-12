"""
List team connections returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.team_connections_api import TeamConnectionsApi

configuration = Configuration()
configuration.unstable_operations["list_team_connections"] = True
with ApiClient(configuration) as api_client:
    api_instance = TeamConnectionsApi(api_client)
    response = api_instance.list_team_connections()

    print(response)
