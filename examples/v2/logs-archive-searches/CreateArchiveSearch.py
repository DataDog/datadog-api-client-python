"""
Create an Archive Search returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archive_searches_api import LogsArchiveSearchesApi
from datadog_api_client.v2.model.archive_search_create_rehydration import ArchiveSearchCreateRehydration
from datadog_api_client.v2.model.archive_search_create_request import ArchiveSearchCreateRequest
from datadog_api_client.v2.model.archive_search_create_request_attributes import ArchiveSearchCreateRequestAttributes
from datadog_api_client.v2.model.archive_search_create_request_data import ArchiveSearchCreateRequestData
from datadog_api_client.v2.model.archive_search_rehydration_tier import ArchiveSearchRehydrationTier
from datadog_api_client.v2.model.archive_search_type import ArchiveSearchType
from datetime import datetime
from dateutil.tz import tzutc

body = ArchiveSearchCreateRequest(
    data=ArchiveSearchCreateRequestData(
        attributes=ArchiveSearchCreateRequestAttributes(
            archive_id="mhmyYmyLTOaFYKvhNadu1w",
            description="Investigating the checkout latency spike.",
            _from=datetime(2026, 1, 1, 0, 0, tzinfo=tzutc()),
            name="checkout-latency-investigation",
            query="service:checkout status:error",
            rehydration=ArchiveSearchCreateRehydration(
                max_rehydrated_events=1000000,
                retention_days=15,
                tier=ArchiveSearchRehydrationTier.STANDARD,
            ),
            to=datetime(2026, 1, 2, 0, 0, tzinfo=tzutc()),
        ),
        type=ArchiveSearchType.ARCHIVE_SEARCH,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_archive_search"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsArchiveSearchesApi(api_client)
    response = api_instance.create_archive_search(body=body)

    print(response)
