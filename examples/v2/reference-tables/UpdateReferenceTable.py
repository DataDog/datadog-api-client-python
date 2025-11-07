"""
Update reference table returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi
from datadog_api_client.v2.model.patch_table_request import PatchTableRequest
from datadog_api_client.v2.model.patch_table_request_data import PatchTableRequestData
from datadog_api_client.v2.model.patch_table_request_data_attributes import PatchTableRequestDataAttributes
from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_cloud_storage import (
    PatchTableRequestDataAttributesFileMetadataCloudStorage,
)
from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details import (
    PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails,
)
from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details_aws_detail import (
    PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail,
)
from datadog_api_client.v2.model.patch_table_request_data_attributes_schema import PatchTableRequestDataAttributesSchema
from datadog_api_client.v2.model.patch_table_request_data_attributes_schema_fields_items import (
    PatchTableRequestDataAttributesSchemaFieldsItems,
)
from datadog_api_client.v2.model.patch_table_request_data_type import PatchTableRequestDataType
from datadog_api_client.v2.model.reference_table_schema_field_type import ReferenceTableSchemaFieldType

body = PatchTableRequest(
    data=PatchTableRequestData(
        attributes=PatchTableRequestDataAttributes(
            description="this is a cloud table generated via a cloud bucket sync",
            file_metadata=PatchTableRequestDataAttributesFileMetadataCloudStorage(
                access_details=PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails(
                    aws_detail=PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail(
                        aws_account_id="test-account-id",
                        aws_bucket_name="test-bucket",
                        file_path="test_rt.csv",
                    ),
                ),
                sync_enabled=True,
            ),
            schema=PatchTableRequestDataAttributesSchema(
                fields=[
                    PatchTableRequestDataAttributesSchemaFieldsItems(
                        name="id",
                        type=ReferenceTableSchemaFieldType.INT32,
                    ),
                    PatchTableRequestDataAttributesSchemaFieldsItems(
                        name="name",
                        type=ReferenceTableSchemaFieldType.STRING,
                    ),
                ],
                primary_keys=[
                    "id",
                ],
            ),
            sync_enabled=False,
            tags=[
                "test_tag",
            ],
        ),
        type=PatchTableRequestDataType.REFERENCE_TABLE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    api_instance.update_reference_table(id="id", body=body)
