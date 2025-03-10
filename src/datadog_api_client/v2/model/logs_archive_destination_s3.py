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
    from datadog_api_client.v2.model.logs_archive_encryption_s3 import LogsArchiveEncryptionS3
    from datadog_api_client.v2.model.logs_archive_integration_s3 import LogsArchiveIntegrationS3
    from datadog_api_client.v2.model.logs_archive_storage_class_s3_type import LogsArchiveStorageClassS3Type
    from datadog_api_client.v2.model.logs_archive_destination_s3_type import LogsArchiveDestinationS3Type


class LogsArchiveDestinationS3(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_encryption_s3 import LogsArchiveEncryptionS3
        from datadog_api_client.v2.model.logs_archive_integration_s3 import LogsArchiveIntegrationS3
        from datadog_api_client.v2.model.logs_archive_storage_class_s3_type import LogsArchiveStorageClassS3Type
        from datadog_api_client.v2.model.logs_archive_destination_s3_type import LogsArchiveDestinationS3Type

        return {
            "bucket": (str,),
            "encryption": (LogsArchiveEncryptionS3,),
            "integration": (LogsArchiveIntegrationS3,),
            "path": (str,),
            "storage_class": (LogsArchiveStorageClassS3Type,),
            "type": (LogsArchiveDestinationS3Type,),
        }

    attribute_map = {
        "bucket": "bucket",
        "encryption": "encryption",
        "integration": "integration",
        "path": "path",
        "storage_class": "storage_class",
        "type": "type",
    }

    def __init__(
        self_,
        bucket: str,
        integration: LogsArchiveIntegrationS3,
        type: LogsArchiveDestinationS3Type,
        encryption: Union[LogsArchiveEncryptionS3, UnsetType] = unset,
        path: Union[str, UnsetType] = unset,
        storage_class: Union[LogsArchiveStorageClassS3Type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The S3 archive destination.

        :param bucket: The bucket where the archive will be stored.
        :type bucket: str

        :param encryption: The S3 encryption settings.
        :type encryption: LogsArchiveEncryptionS3, optional

        :param integration: The S3 Archive's integration destination.
        :type integration: LogsArchiveIntegrationS3

        :param path: The archive path.
        :type path: str, optional

        :param storage_class: The storage class where the archive will be stored.
        :type storage_class: LogsArchiveStorageClassS3Type, optional

        :param type: Type of the S3 archive destination.
        :type type: LogsArchiveDestinationS3Type
        """
        if encryption is not unset:
            kwargs["encryption"] = encryption
        if path is not unset:
            kwargs["path"] = path
        if storage_class is not unset:
            kwargs["storage_class"] = storage_class
        super().__init__(kwargs)

        self_.bucket = bucket
        self_.integration = integration
        self_.type = type
