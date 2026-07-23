"""
Delete a RUM operation returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_operations_api import RUMOperationsApi

configuration = Configuration()
configuration.unstable_operations["delete_rum_operation"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMOperationsApi(api_client)
    api_instance.delete_rum_operation(
        operation_id="operation_id",
    )
