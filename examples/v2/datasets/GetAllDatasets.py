"""
Get all datasets returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.get_all_datasets()

    print(response)
