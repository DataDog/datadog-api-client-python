# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_one_of_access_details import (
        TableResultV2DataAttributesFileMetadataOneOfAccessDetails,
    )
    from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_cloud_storage_error_type import (
        TableResultV2DataAttributesFileMetadataCloudStorageErrorType,
    )


class TableResultV2DataAttributesFileMetadataCloudStorage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_one_of_access_details import (
            TableResultV2DataAttributesFileMetadataOneOfAccessDetails,
        )
        from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_cloud_storage_error_type import (
            TableResultV2DataAttributesFileMetadataCloudStorageErrorType,
        )

        return {
            "access_details": (TableResultV2DataAttributesFileMetadataOneOfAccessDetails,),
            "error_message": (str,),
            "error_row_count": (int,),
            "error_type": (TableResultV2DataAttributesFileMetadataCloudStorageErrorType,),
            "sync_enabled": (bool,),
        }

    attribute_map = {
        "access_details": "access_details",
        "error_message": "error_message",
        "error_row_count": "error_row_count",
        "error_type": "error_type",
        "sync_enabled": "sync_enabled",
    }

    def __init__(
        self_,
        access_details: Union[TableResultV2DataAttributesFileMetadataOneOfAccessDetails, UnsetType] = unset,
        error_message: Union[str, UnsetType] = unset,
        error_row_count: Union[int, UnsetType] = unset,
        error_type: Union[TableResultV2DataAttributesFileMetadataCloudStorageErrorType, UnsetType] = unset,
        sync_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        File metadata for reference tables created by cloud storage.

        :param access_details: The definition of ``TableResultV2DataAttributesFileMetadataOneOfAccessDetails`` object.
        :type access_details: TableResultV2DataAttributesFileMetadataOneOfAccessDetails, optional

        :param error_message: The error message returned from the sync.
        :type error_message: str, optional

        :param error_row_count: The number of rows that failed to sync.
        :type error_row_count: int, optional

        :param error_type: The type of error that occurred during file processing. This field provides high-level error categories for easier troubleshooting and is only present when there are errors.
        :type error_type: TableResultV2DataAttributesFileMetadataCloudStorageErrorType, optional

        :param sync_enabled: Whether this table is synced automatically.
        :type sync_enabled: bool, optional
        """
        if access_details is not unset:
            kwargs["access_details"] = access_details
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if error_row_count is not unset:
            kwargs["error_row_count"] = error_row_count
        if error_type is not unset:
            kwargs["error_type"] = error_type
        if sync_enabled is not unset:
            kwargs["sync_enabled"] = sync_enabled
        super().__init__(kwargs)
