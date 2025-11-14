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
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_azure_detail import (
    CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail,
)
from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_gcp_detail import (
    CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail,
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
            file_metadata=CreateTableRequestDataAttributesFileMetadataCloudStorage(
                access_details=CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails(
                    aws_detail=CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail(
                        aws_account_id="123456789000",
                        aws_bucket_name="example-data-bucket",
                        file_path="reference-tables/users.csv",
                    ),
                    azure_detail=CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail(
                        azure_client_id="aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
                        azure_container_name="reference-data",
                        azure_storage_account_name="examplestorageaccount",
                        azure_tenant_id="cccccccc-4444-5555-6666-dddddddddddd",
                        file_path="tables/users.csv",
                    ),
                    gcp_detail=CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail(
                        file_path="data/reference_tables/users.csv",
                        gcp_bucket_name="example-data-bucket",
                        gcp_project_id="example-gcp-project-12345",
                        gcp_service_account_email="example-service@example-gcp-project-12345.iam.gserviceaccount.com",
                    ),
                ),
                sync_enabled=False,
            ),
            schema=CreateTableRequestDataAttributesSchema(
                fields=[
                    CreateTableRequestDataAttributesSchemaFieldsItems(
                        name="field_1",
                        type=ReferenceTableSchemaFieldType.STRING,
                    ),
                ],
                primary_keys=[
                    "field_1",
                ],
            ),
            source=ReferenceTableCreateSourceType.LOCAL_FILE,
            table_name="table_1",
            tags=[
                "tag_1",
                "tag_2",
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
