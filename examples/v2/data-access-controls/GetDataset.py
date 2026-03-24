"""
Get a Data Access Control dataset by ID returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.data_access_controls_api import DataAccessControlsApi

configuration = Configuration()
configuration.unstable_operations["get_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DataAccessControlsApi(api_client)
    response = api_instance.get_dataset(
        dataset_id="dataset_id",
    )

    print(response)
