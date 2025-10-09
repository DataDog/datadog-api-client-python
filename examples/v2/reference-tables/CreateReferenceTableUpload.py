"""
Create reference table upload returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.create_upload_request import CreateUploadRequest
from datadog_api_client.v2.model.create_upload_request_data import CreateUploadRequestData
from datadog_api_client.v2.model.create_upload_request_data_attributes import CreateUploadRequestDataAttributes
from datadog_api_client.v2.model.create_upload_request_data_type import CreateUploadRequestDataType

body = CreateUploadRequest(
    data=CreateUploadRequestData(
        attributes=CreateUploadRequestDataAttributes(
            headers=[
                "id",
                "name",
                "value",
            ],
            table_name="test_upload_table_Example-Reference-Table",
            part_count=1,
            part_size=1024,
        ),
        type=CreateUploadRequestDataType.UPLOAD,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    response = api_instance.create_reference_table_upload(body=body)

    print(response)
