"""
Delete a dataset returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi

# there is a valid "dataset" in the system
DATASET_DATA_ID = environ["DATASET_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    api_instance.delete_dataset(
        dataset_id=DATASET_DATA_ID,
    )
