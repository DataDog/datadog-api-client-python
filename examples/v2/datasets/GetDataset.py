"""
Get a single dataset by ID returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.get_dataset(
        dataset_id="dataset_id",
    )

    print(response)
