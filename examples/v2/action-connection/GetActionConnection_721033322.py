"""
Get a GCP Action Connection preserves AWS Secrets Manager references
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

# there is a valid "gcp_action_connection" in the system
GCP_ACTION_CONNECTION_DATA_ID = environ["GCP_ACTION_CONNECTION_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.get_action_connection(
        connection_id=GCP_ACTION_CONNECTION_DATA_ID,
    )

    print(response)
