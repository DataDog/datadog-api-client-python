"""
List dataset restrictions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dataset_restrictions_api import DatasetRestrictionsApi

configuration = Configuration()
configuration.unstable_operations["list_dataset_restrictions"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetRestrictionsApi(api_client)
    response = api_instance.list_dataset_restrictions()

    print(response)
