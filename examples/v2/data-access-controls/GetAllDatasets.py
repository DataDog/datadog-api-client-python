"""
Get all Data Access Control datasets returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.data_access_controls_api import DataAccessControlsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DataAccessControlsApi(api_client)
    response = api_instance.get_all_datasets()

    print(response)
