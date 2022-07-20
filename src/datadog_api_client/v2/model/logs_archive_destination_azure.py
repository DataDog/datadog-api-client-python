# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsArchiveDestinationAzure(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_integration_azure import LogsArchiveIntegrationAzure
        from datadog_api_client.v2.model.logs_archive_destination_azure_type import LogsArchiveDestinationAzureType

        return {
            "container": (str,),
            "integration": (LogsArchiveIntegrationAzure,),
            "path": (str,),
            "region": (str,),
            "storage_account": (str,),
            "type": (LogsArchiveDestinationAzureType,),
        }

    attribute_map = {
        "container": "container",
        "integration": "integration",
        "path": "path",
        "region": "region",
        "storage_account": "storage_account",
        "type": "type",
    }

    def __init__(self, container, integration, storage_account, type, *args, **kwargs):
        """
        The Azure archive destination.

        :param container: The container where the archive will be stored.
        :type container: str

        :param integration: The Azure archive's integration destination.
        :type integration: LogsArchiveIntegrationAzure

        :param path: The archive path.
        :type path: str, optional

        :param region: The region where the archive will be stored.
        :type region: str, optional

        :param storage_account: The associated storage account.
        :type storage_account: str

        :param type: Type of the Azure archive destination.
        :type type: LogsArchiveDestinationAzureType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.container = container
        self.integration = integration
        self.storage_account = storage_account
        self.type = type

    @classmethod
    def _from_openapi_data(cls, container, integration, storage_account, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsArchiveDestinationAzure, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.container = container
        self.integration = integration
        self.storage_account = storage_account
        self.type = type
        return self
