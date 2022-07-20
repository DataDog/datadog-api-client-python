"""
List read roles for an archive returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.list_archive_read_roles(
        archive_id="archive_id",
    )

    print(response)
