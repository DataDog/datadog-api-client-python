"""
Delete a Data Access Control dataset returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.data_access_controls_api import DataAccessControlsApi

# there is a valid "dataset" in the system
DATASET_DATA_ID = environ["DATASET_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DataAccessControlsApi(api_client)
    api_instance.delete_dataset(
        dataset_id=DATASET_DATA_ID,
    )
