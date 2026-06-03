"""
Get the RUM configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_config_api import RumConfigApi

configuration = Configuration()
configuration.unstable_operations["get_rum_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumConfigApi(api_client)
    response = api_instance.get_rum_config()

    print(response)
