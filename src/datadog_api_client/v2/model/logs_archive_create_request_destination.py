# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v2.model.logs_archive_destination_azure import LogsArchiveDestinationAzure
    from datadog_api_client.v2.model.logs_archive_destination_gcs import LogsArchiveDestinationGCS
    from datadog_api_client.v2.model.logs_archive_destination_s3 import LogsArchiveDestinationS3
    from datadog_api_client.v2.model.logs_archive_destination_s3_type import LogsArchiveDestinationS3Type
    from datadog_api_client.v2.model.logs_archive_integration_s3 import LogsArchiveIntegrationS3

    globals()["LogsArchiveDestinationAzure"] = LogsArchiveDestinationAzure
    globals()["LogsArchiveDestinationGCS"] = LogsArchiveDestinationGCS
    globals()["LogsArchiveDestinationS3"] = LogsArchiveDestinationS3
    globals()["LogsArchiveDestinationS3Type"] = LogsArchiveDestinationS3Type
    globals()["LogsArchiveIntegrationS3"] = LogsArchiveIntegrationS3


class LogsArchiveCreateRequestDestination(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {}

    def __init__(self, *args, **kwargs):
        """LogsArchiveCreateRequestDestination - a model defined in OpenAPI

        Keyword Args:
            path (str): [optional] The archive path.
            region (str): [optional] The region where the archive will be stored.
            container (str): [optional] The container where the archive will be stored.
            integration (LogsArchiveIntegrationS3): [optional]
            storage_account (str): [optional] The associated storage account.
            type (LogsArchiveDestinationS3Type): [optional]
            bucket (str): [optional] The bucket where the archive will be stored.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsArchiveCreateRequestDestination, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                LogsArchiveDestinationAzure,
                LogsArchiveDestinationGCS,
                LogsArchiveDestinationS3,
            ],
        }
