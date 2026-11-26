"""
Delete a RUM operation link returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_operations_api import RUMOperationsApi

# there is a valid "rum_operation_strong_link" in the system
RUM_OPERATION_STRONG_LINK_DATA_ATTRIBUTES_FEATURE_ID = environ["RUM_OPERATION_STRONG_LINK_DATA_ATTRIBUTES_FEATURE_ID"]
RUM_OPERATION_STRONG_LINK_DATA_ATTRIBUTES_OPERATION_ID = environ[
    "RUM_OPERATION_STRONG_LINK_DATA_ATTRIBUTES_OPERATION_ID"
]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMOperationsApi(api_client)
    api_instance.delete_rum_operation_strong_link(
        rum_operation_id=RUM_OPERATION_STRONG_LINK_DATA_ATTRIBUTES_OPERATION_ID,
        feature_id=RUM_OPERATION_STRONG_LINK_DATA_ATTRIBUTES_FEATURE_ID,
    )
