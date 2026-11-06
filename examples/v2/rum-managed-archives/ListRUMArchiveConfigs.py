"""
List archive configurations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_managed_archives_api import RUMManagedArchivesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMManagedArchivesApi(api_client)
    response = api_instance.list_rum_archive_configs(
        page_number=0,
        page_size=1,
    )

    print(response)
