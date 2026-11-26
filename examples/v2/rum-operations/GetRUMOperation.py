"""
Get a RUM operation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_operations_api import RUMOperationsApi

# there is a valid "rum_operation" in the system
RUM_OPERATION_DATA_ID = environ["RUM_OPERATION_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMOperationsApi(api_client)
    response = api_instance.get_rum_operation(
        rum_operation_id=RUM_OPERATION_DATA_ID,
    )

    print(response)
