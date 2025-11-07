# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TableResultV2DataAttributesFileMetadata(ModelComposed):
    def __init__(self, **kwargs):
        """
        Metadata specifying where and how to access the reference table's data file.

        :param access_details: Cloud storage access configuration for the reference table data file.
        :type access_details: TableResultV2DataAttributesFileMetadataOneOfAccessDetails

        :param error_message: The error message returned from the sync.
        :type error_message: str, optional

        :param error_row_count: The number of rows that failed to sync.
        :type error_row_count: int, optional

        :param error_type: The type of error that occurred during file processing. This field provides high-level error categories for easier troubleshooting and is only present when there are errors.
        :type error_type: TableResultV2DataAttributesFileMetadataCloudStorageErrorType, optional

        :param sync_enabled: Whether this table is synced automatically.
        :type sync_enabled: bool, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_cloud_storage import (
            TableResultV2DataAttributesFileMetadataCloudStorage,
        )
        from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_local_file import (
            TableResultV2DataAttributesFileMetadataLocalFile,
        )

        return {
            "oneOf": [
                TableResultV2DataAttributesFileMetadataCloudStorage,
                TableResultV2DataAttributesFileMetadataLocalFile,
            ],
        }
