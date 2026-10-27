"""
Rehydrate an Archive Search returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archive_searches_api import LogsArchiveSearchesApi
from datadog_api_client.v2.model.archive_search_rehydrate_request import ArchiveSearchRehydrateRequest
from datadog_api_client.v2.model.archive_search_rehydrate_request_attributes import (
    ArchiveSearchRehydrateRequestAttributes,
)
from datadog_api_client.v2.model.archive_search_rehydrate_request_data import ArchiveSearchRehydrateRequestData
from datadog_api_client.v2.model.archive_search_rehydrate_request_rehydration import (
    ArchiveSearchRehydrateRequestRehydration,
)
from datadog_api_client.v2.model.archive_search_rehydration_tier import ArchiveSearchRehydrationTier
from datadog_api_client.v2.model.archive_search_type import ArchiveSearchType

body = ArchiveSearchRehydrateRequest(
    data=ArchiveSearchRehydrateRequestData(
        attributes=ArchiveSearchRehydrateRequestAttributes(
            rehydration=ArchiveSearchRehydrateRequestRehydration(
                retention_days=15,
                tier=ArchiveSearchRehydrationTier.STANDARD,
            ),
        ),
        type=ArchiveSearchType.ARCHIVE_SEARCH,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["rehydrate_archive_search"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsArchiveSearchesApi(api_client)
    response = api_instance.rehydrate_archive_search(archive_search_id="archive_search_id", body=body)

    print(response)
