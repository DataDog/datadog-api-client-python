"""
Delete a Data Access Control dataset returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.data_access_controls_api import DataAccessControlsApi

configuration = Configuration()
configuration.unstable_operations["delete_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DataAccessControlsApi(api_client)
    api_instance.delete_dataset(
        dataset_id="dataset_id",
    )
