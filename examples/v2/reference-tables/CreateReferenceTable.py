"""
Create reference table returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.create_table_request import CreateTableRequest
from datadog_api_client.v2.model.create_table_request_data import CreateTableRequestData
from datadog_api_client.v2.model.create_table_request_data_attributes import CreateTableRequestDataAttributes
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_cloud_storage import (
    CreateTableRequestDataAttributesFileMetadataCloudStorage,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details import (
    CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_aws_detail import (
    CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail,
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
            description="this is a cloud table generated via a cloud bucket sync",
            file_metadata=CreateTableRequestDataAttributesFileMetadataCloudStorage(
                access_details=CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails(
                    aws_detail=CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail(
                        aws_account_id="test-account-id",
                        aws_bucket_name="test-bucket",
                        file_path="test_rt.csv",
                    ),
                ),
                sync_enabled=True,
            ),
            schema=CreateTableRequestDataAttributesSchema(
                fields=[
                    CreateTableRequestDataAttributesSchemaFieldsItems(
                        name="name",
                        type=ReferenceTableSchemaFieldType.STRING,
                    ),
                    CreateTableRequestDataAttributesSchemaFieldsItems(
                        name="account_id",
                        type=ReferenceTableSchemaFieldType.STRING,
                    ),
                ],
                primary_keys=[
                    "account_id",
                ],
            ),
            source=ReferenceTableCreateSourceType.S3,
            table_name="test_reference_table",
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
