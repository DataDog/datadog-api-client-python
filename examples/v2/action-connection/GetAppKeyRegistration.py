"""
Get an existing App Key Registration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.get_app_key_registration(
        app_key_id="b7feea52-994e-4714-a100-1bd9eff5aee1",
    )

    print(response)
