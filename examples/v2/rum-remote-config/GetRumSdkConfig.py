"""
Get a RUM SDK configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_remote_config_api import RUMRemoteConfigApi

configuration = Configuration()
configuration.unstable_operations["get_rum_sdk_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMRemoteConfigApi(api_client)
    response = api_instance.get_rum_sdk_config(
        config_id="config_id",
    )

    print(response)
