"""
Forces a data deletion request returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.data_deletion_api import DataDeletionApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["force_data_deletion_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = DataDeletionApi(api_client)
    response = api_instance.force_data_deletion_request(
        id="id",
    )

    print(response)
