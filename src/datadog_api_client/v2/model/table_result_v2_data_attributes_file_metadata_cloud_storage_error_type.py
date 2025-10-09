# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TableResultV2DataAttributesFileMetadataCloudStorageErrorType(ModelSimple):
    """
    The type of error that occurred during file processing. This field provides high-level error categories for easier troubleshooting and is only present when there are errors.

    :param value: Must be one of ["TABLE_SCHEMA_ERROR", "FILE_FORMAT_ERROR", "CONFIGURATION_ERROR", "QUOTA_EXCEEDED", "CONFLICT_ERROR", "VALIDATION_ERROR", "STATE_ERROR", "OPERATION_ERROR", "SYSTEM_ERROR"].
    :type value: str
    """

    allowed_values = {
        "TABLE_SCHEMA_ERROR",
        "FILE_FORMAT_ERROR",
        "CONFIGURATION_ERROR",
        "QUOTA_EXCEEDED",
        "CONFLICT_ERROR",
        "VALIDATION_ERROR",
        "STATE_ERROR",
        "OPERATION_ERROR",
        "SYSTEM_ERROR",
    }
    TABLE_SCHEMA_ERROR: ClassVar["TableResultV2DataAttributesFileMetadataCloudStorageErrorType"]
    FILE_FORMAT_ERROR: ClassVar["TableResultV2DataAttributesFileMetadataCloudStorageErrorType"]
    CONFIGURATION_ERROR: ClassVar["TableResultV2DataAttributesFileMetadataCloudStorageErrorType"]
    QUOTA_EXCEEDED: ClassVar["TableResultV2DataAttributesFileMetadataCloudStorageErrorType"]
    CONFLICT_ERROR: ClassVar["TableResultV2DataAttributesFileMetadataCloudStorageErrorType"]
    VALIDATION_ERROR: ClassVar["TableResultV2DataAttributesFileMetadataCloudStorageErrorType"]
    STATE_ERROR: ClassVar["TableResultV2DataAttributesFileMetadataCloudStorageErrorType"]
    OPERATION_ERROR: ClassVar["TableResultV2DataAttributesFileMetadataCloudStorageErrorType"]
    SYSTEM_ERROR: ClassVar["TableResultV2DataAttributesFileMetadataCloudStorageErrorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TableResultV2DataAttributesFileMetadataCloudStorageErrorType.TABLE_SCHEMA_ERROR = (
    TableResultV2DataAttributesFileMetadataCloudStorageErrorType("TABLE_SCHEMA_ERROR")
)
TableResultV2DataAttributesFileMetadataCloudStorageErrorType.FILE_FORMAT_ERROR = (
    TableResultV2DataAttributesFileMetadataCloudStorageErrorType("FILE_FORMAT_ERROR")
)
TableResultV2DataAttributesFileMetadataCloudStorageErrorType.CONFIGURATION_ERROR = (
    TableResultV2DataAttributesFileMetadataCloudStorageErrorType("CONFIGURATION_ERROR")
)
TableResultV2DataAttributesFileMetadataCloudStorageErrorType.QUOTA_EXCEEDED = (
    TableResultV2DataAttributesFileMetadataCloudStorageErrorType("QUOTA_EXCEEDED")
)
TableResultV2DataAttributesFileMetadataCloudStorageErrorType.CONFLICT_ERROR = (
    TableResultV2DataAttributesFileMetadataCloudStorageErrorType("CONFLICT_ERROR")
)
TableResultV2DataAttributesFileMetadataCloudStorageErrorType.VALIDATION_ERROR = (
    TableResultV2DataAttributesFileMetadataCloudStorageErrorType("VALIDATION_ERROR")
)
TableResultV2DataAttributesFileMetadataCloudStorageErrorType.STATE_ERROR = (
    TableResultV2DataAttributesFileMetadataCloudStorageErrorType("STATE_ERROR")
)
TableResultV2DataAttributesFileMetadataCloudStorageErrorType.OPERATION_ERROR = (
    TableResultV2DataAttributesFileMetadataCloudStorageErrorType("OPERATION_ERROR")
)
TableResultV2DataAttributesFileMetadataCloudStorageErrorType.SYSTEM_ERROR = (
    TableResultV2DataAttributesFileMetadataCloudStorageErrorType("SYSTEM_ERROR")
)
