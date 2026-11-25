"""
Search archived sessions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_recovery_api import RUMRecoveryApi
from datadog_api_client.v2.model.rum_archive_sessions_search_attributes import RUMArchiveSessionsSearchAttributes
from datadog_api_client.v2.model.rum_archive_sessions_search_data import RUMArchiveSessionsSearchData
from datadog_api_client.v2.model.rum_archive_sessions_search_request import RUMArchiveSessionsSearchRequest

body = RUMArchiveSessionsSearchRequest(
    data=RUMArchiveSessionsSearchData(
        attributes=RUMArchiveSessionsSearchAttributes(
            cursor="example",
            _from=1789905600000,
            hide_retained=False,
            limit=0,
            query="service:web",
            to=1789992000000,
        ),
        id="11111111-1111-4111-8111-111111111111",
        type="rum_archive_sessions_request",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRecoveryApi(api_client)
    response = api_instance.search_rum_archive_sessions(body=body)

    print(response)
