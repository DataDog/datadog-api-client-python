"""
Create reference table with upload returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.create_table_request import CreateTableRequest
from datadog_api_client.v2.model.create_table_request_data import CreateTableRequestData
from datadog_api_client.v2.model.create_table_request_data_attributes import CreateTableRequestDataAttributes
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_local_file import (
    CreateTableRequestDataAttributesFileMetadataLocalFile,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_schema import (
    CreateTableRequestDataAttributesSchema,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_schema_fields_items import (
    CreateTableRequestDataAttributesSchemaFieldsItems,
)
from datadog_api_client.v2.model.create_table_request_data_type import CreateTableRequestDataType
from datadog_api_client.v2.model.reference_table_create_source_type import ReferenceTableCreateSourceType
from datadog_api_client.v2.model.reference_table_schema_field_type import ReferenceTableSchemaFieldType

body = CreateTableRequest(
    data=CreateTableRequestData(
        attributes=CreateTableRequestDataAttributes(
            description="Test reference table created via BDD test Example-Reference-Table",
            source=ReferenceTableCreateSourceType.LOCAL_FILE,
            file_metadata=CreateTableRequestDataAttributesFileMetadataLocalFile(
                upload_id="test-upload-id-Example-Reference-Table",
            ),
            schema=CreateTableRequestDataAttributesSchema(
                fields=[
                    CreateTableRequestDataAttributesSchemaFieldsItems(
                        name="id",
                        type=ReferenceTableSchemaFieldType.STRING,
                    ),
                    CreateTableRequestDataAttributesSchemaFieldsItems(
                        name="name",
                        type=ReferenceTableSchemaFieldType.STRING,
                    ),
                    CreateTableRequestDataAttributesSchemaFieldsItems(
                        name="value",
                        type=ReferenceTableSchemaFieldType.INT32,
                    ),
                ],
                primary_keys=[
                    "id",
                ],
            ),
            table_name="test_reference_table_Example-Reference-Table",
            tags=[
                "test_tag",
            ],
        ),
        type=CreateTableRequestDataType.REFERENCE_TABLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    response = api_instance.create_reference_table(body=body)

    print(response)
