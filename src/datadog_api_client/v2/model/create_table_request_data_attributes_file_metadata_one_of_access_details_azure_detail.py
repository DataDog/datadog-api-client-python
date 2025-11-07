# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "azure_client_id": (str,),
            "azure_container_name": (str,),
            "azure_storage_account_name": (str,),
            "azure_tenant_id": (str,),
            "file_path": (str,),
        }

    attribute_map = {
        "azure_client_id": "azure_client_id",
        "azure_container_name": "azure_container_name",
        "azure_storage_account_name": "azure_storage_account_name",
        "azure_tenant_id": "azure_tenant_id",
        "file_path": "file_path",
    }

    def __init__(
        self_,
        azure_client_id: str,
        azure_container_name: str,
        azure_storage_account_name: str,
        azure_tenant_id: str,
        file_path: str,
        **kwargs,
    ):
        """
        Azure Blob Storage access configuration.

        :param azure_client_id: Azure service principal (application) client ID with permissions to read from the container.
        :type azure_client_id: str

        :param azure_container_name: Azure Blob Storage container containing the CSV file.
        :type azure_container_name: str

        :param azure_storage_account_name: Azure storage account where the container is located.
        :type azure_storage_account_name: str

        :param azure_tenant_id: Azure Active Directory tenant ID.
        :type azure_tenant_id: str

        :param file_path: The relative file path from the Azure container root to the CSV file.
        :type file_path: str
        """
        super().__init__(kwargs)

        self_.azure_client_id = azure_client_id
        self_.azure_container_name = azure_container_name
        self_.azure_storage_account_name = azure_storage_account_name
        self_.azure_tenant_id = azure_tenant_id
        self_.file_path = file_path
