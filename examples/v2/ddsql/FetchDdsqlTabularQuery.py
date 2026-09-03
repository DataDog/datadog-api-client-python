"""
Fetch the result of a DDSQL query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ddsql_api import DDSQLApi
from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request import DdsqlTabularQueryFetchRequest
from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request_attributes import (
    DdsqlTabularQueryFetchRequestAttributes,
)
from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request_data import DdsqlTabularQueryFetchRequestData
from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request_type import DdsqlTabularQueryFetchRequestType

body = DdsqlTabularQueryFetchRequest(
    data=DdsqlTabularQueryFetchRequestData(
        attributes=DdsqlTabularQueryFetchRequestAttributes(
            query_id="eyJxdWVyeSI6ICJTRUxFQ1QgKiBGUk9NIGxvZ3MifQ==",
        ),
        type=DdsqlTabularQueryFetchRequestType.DDSQL_QUERY_FETCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DDSQLApi(api_client)
    response = api_instance.fetch_ddsql_tabular_query(body=body)

    print(response)
