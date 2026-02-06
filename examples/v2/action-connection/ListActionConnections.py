"""
List action connections returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
configuration.unstable_operations["list_action_connections"] = True
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.list_action_connections()

    print(response)
