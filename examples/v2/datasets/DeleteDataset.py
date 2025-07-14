"""
Delete a dataset returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    api_instance.delete_dataset(
        dataset_id="dataset_id",
    )
