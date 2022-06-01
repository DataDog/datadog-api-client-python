# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsArchiveDestinationS3(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_integration_s3 import LogsArchiveIntegrationS3
        from datadog_api_client.v2.model.logs_archive_destination_s3_type import LogsArchiveDestinationS3Type

        return {
            "bucket": (str,),
            "integration": (LogsArchiveIntegrationS3,),
            "path": (str,),
            "type": (LogsArchiveDestinationS3Type,),
        }

    attribute_map = {
        "bucket": "bucket",
        "integration": "integration",
        "path": "path",
        "type": "type",
    }

    def __init__(self, bucket, integration, type, *args, **kwargs):
        """
        The S3 archive destination.

        :param bucket: The bucket where the archive will be stored.
        :type bucket: str

        :param integration: The S3 Archive's integration destination.
        :type integration: LogsArchiveIntegrationS3

        :param path: The archive path.
        :type path: str, optional

        :param type: Type of the S3 archive destination.
        :type type: LogsArchiveDestinationS3Type
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.bucket = bucket
        self.integration = integration
        self.type = type

    @classmethod
    def _from_openapi_data(cls, bucket, integration, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsArchiveDestinationS3, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.bucket = bucket
        self.integration = integration
        self.type = type
        return self
