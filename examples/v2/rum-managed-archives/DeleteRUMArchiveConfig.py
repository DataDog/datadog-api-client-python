"""
Delete an archive configuration returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_managed_archives_api import RUMManagedArchivesApi
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMManagedArchivesApi(api_client)
    api_instance.delete_rum_archive_config(
        app_id=UUID("a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"),
    )
