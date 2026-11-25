"""
Search archived sessions returns canonical data and first-page metadata
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_recovery_api import RUMRecoveryApi
from datadog_api_client.v2.model.rum_archive_sessions_search_attributes import RUMArchiveSessionsSearchAttributes
from datadog_api_client.v2.model.rum_archive_sessions_search_data import RUMArchiveSessionsSearchData
from datadog_api_client.v2.model.rum_archive_sessions_search_request import RUMArchiveSessionsSearchRequest

body = RUMArchiveSessionsSearchRequest(
    data=RUMArchiveSessionsSearchData(
        type="rum_archive_sessions_request",
        attributes=RUMArchiveSessionsSearchAttributes(
            query="service:rum18600-fixture",
            _from=1636024271000,
            to=1636629071000,
            limit=1,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRecoveryApi(api_client)
    response = api_instance.search_rum_archive_sessions(body=body)

    print(response)
