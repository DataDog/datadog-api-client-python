"""
List RUM operation strong links returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_operations_api import RUMOperationsApi

configuration = Configuration()
configuration.unstable_operations["list_rum_operation_strong_links"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMOperationsApi(api_client)
    response = api_instance.list_rum_operation_strong_links()

    print(response)
