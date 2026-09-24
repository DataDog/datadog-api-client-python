"""
Get the RUM configuration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_config_api import RUMConfigApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_rum_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMConfigApi(api_client)
    response = api_instance.get_rum_config()

    print(response)
