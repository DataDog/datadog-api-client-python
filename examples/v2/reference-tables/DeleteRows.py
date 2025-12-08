"""
Delete rows returns "Rows deleted successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.batch_delete_rows_request_array import BatchDeleteRowsRequestArray
from datadog_api_client.v2.model.batch_delete_rows_request_data import BatchDeleteRowsRequestData
from datadog_api_client.v2.model.table_row_resource_data_type import TableRowResourceDataType

body = BatchDeleteRowsRequestArray(
    data=[
        BatchDeleteRowsRequestData(
            id="primary_key_value",
            type=TableRowResourceDataType.ROW,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    api_instance.delete_rows(id="id", body=body)
