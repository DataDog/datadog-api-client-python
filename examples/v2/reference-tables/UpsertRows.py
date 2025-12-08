"""
Upsert rows returns "Rows created or updated successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.batch_upsert_rows_request_array import BatchUpsertRowsRequestArray
from datadog_api_client.v2.model.batch_upsert_rows_request_data import BatchUpsertRowsRequestData
from datadog_api_client.v2.model.batch_upsert_rows_request_data_attributes import BatchUpsertRowsRequestDataAttributes
from datadog_api_client.v2.model.table_row_resource_data_type import TableRowResourceDataType

body = BatchUpsertRowsRequestArray(
    data=[
        BatchUpsertRowsRequestData(
            attributes=BatchUpsertRowsRequestDataAttributes(
                values=dict(
                    example_key_value="primary_key_value",
                    name="row_name",
                ),
            ),
            id="primary_key_value",
            type=TableRowResourceDataType.ROW,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    api_instance.upsert_rows(id="id", body=body)
