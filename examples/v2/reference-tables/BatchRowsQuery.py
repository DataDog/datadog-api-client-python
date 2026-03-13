"""
Batch rows query returns "Successfully retrieved rows. Some or all requested rows were found. Response includes found
rows in the included section." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.batch_rows_query_data_type import BatchRowsQueryDataType
from datadog_api_client.v2.model.batch_rows_query_request import BatchRowsQueryRequest
from datadog_api_client.v2.model.batch_rows_query_request_data import BatchRowsQueryRequestData
from datadog_api_client.v2.model.batch_rows_query_request_data_attributes import BatchRowsQueryRequestDataAttributes

body = BatchRowsQueryRequest(
    data=BatchRowsQueryRequestData(
        attributes=BatchRowsQueryRequestDataAttributes(
            row_ids=[
                "row_id_1",
                "row_id_2",
            ],
            table_id="00000000-0000-0000-0000-000000000000",
        ),
        type=BatchRowsQueryDataType.REFERENCE_TABLES_BATCH_ROWS_QUERY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    response = api_instance.batch_rows_query(body=body)

    print(response)
