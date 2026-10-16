"""
Execute a tabular DDSQL query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ddsql_api import DDSQLApi
from datadog_api_client.v2.model.ddsql_tabular_query_request import DdsqlTabularQueryRequest
from datadog_api_client.v2.model.ddsql_tabular_query_request_attributes import DdsqlTabularQueryRequestAttributes
from datadog_api_client.v2.model.ddsql_tabular_query_request_data import DdsqlTabularQueryRequestData
from datadog_api_client.v2.model.ddsql_tabular_query_request_type import DdsqlTabularQueryRequestType
from datadog_api_client.v2.model.ddsql_tabular_query_time_window import DdsqlTabularQueryTimeWindow

body = DdsqlTabularQueryRequest(
    data=DdsqlTabularQueryRequestData(
        attributes=DdsqlTabularQueryRequestAttributes(
            query="SELECT cloud_provider, count(*) FROM dd.hosts group by cloud_provider",
            row_limit=1000,
            time=DdsqlTabularQueryTimeWindow(
                from_timestamp=1736942400000,
                to_timestamp=1736946000000,
            ),
        ),
        type=DdsqlTabularQueryRequestType.DDSQL_QUERY_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DDSQLApi(api_client)
    response = api_instance.execute_ddsql_tabular_query(body=body)

    print(response)
