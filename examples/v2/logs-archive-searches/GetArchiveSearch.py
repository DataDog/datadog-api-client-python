"""
Get an Archive Search returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archive_searches_api import LogsArchiveSearchesApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_archive_search"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsArchiveSearchesApi(api_client)
    response = api_instance.get_archive_search(
        archive_search_id="archive_search_id",
    )

    print(response)
