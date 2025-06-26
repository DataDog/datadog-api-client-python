"""
Unregister an App Key returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    api_instance.unregister_app_key(
        app_key_id="57cc69ae-9214-4ecc-8df8-43ecc1d92d99",
    )
