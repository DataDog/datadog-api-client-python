"""
Gets a list of data deletion requests returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.data_deletion_api import DataDeletionApi

configuration = Configuration()
configuration.unstable_operations["get_data_deletion_requests"] = True
with ApiClient(configuration) as api_client:
    api_instance = DataDeletionApi(api_client)
    response = api_instance.get_data_deletion_requests()

    print(response)
