"""
Get an existing Action Connection returns "Successfully got an Action Connection." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.get_action_connection(
        connection_id="connection_id",
    )

    print(response)
