"""
Register a new App Key returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.register_app_key(
        app_key_id="b7feea52-994e-4714-a100-1bd9eff5aee1",
    )

    print(response)
