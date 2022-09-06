# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsArchiveDestinationGCS(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_integration_gcs import LogsArchiveIntegrationGCS
        from datadog_api_client.v2.model.logs_archive_destination_gcs_type import LogsArchiveDestinationGCSType

        return {
            "bucket": (str,),
            "integration": (LogsArchiveIntegrationGCS,),
            "path": (str,),
            "type": (LogsArchiveDestinationGCSType,),
        }

    attribute_map = {
        "bucket": "bucket",
        "integration": "integration",
        "path": "path",
        "type": "type",
    }

    def __init__(self_, bucket, integration, type, *args, **kwargs):
        """
        The GCS archive destination.

        :param bucket: The bucket where the archive will be stored.
        :type bucket: str

        :param integration: The GCS archive's integration destination.
        :type integration: LogsArchiveIntegrationGCS

        :param path: The archive path.
        :type path: str, optional

        :param type: Type of the GCS archive destination.
        :type type: LogsArchiveDestinationGCSType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.bucket = bucket
        self_.integration = integration
        self_.type = type
