"""
Delete a Storage Management configuration returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.storage_management_api import StorageManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StorageManagementApi(api_client)
    api_instance.delete_sync_config(
        id="id",
    )
