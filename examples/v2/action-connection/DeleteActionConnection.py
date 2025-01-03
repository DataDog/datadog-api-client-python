"""
Delete an existing Action Connection returns "The resource was deleted successfully." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    api_instance.delete_action_connection(
        connection_id="connection_id",
    )
