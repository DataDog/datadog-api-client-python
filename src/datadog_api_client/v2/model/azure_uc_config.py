# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AzureUCConfig(ModelNormal):
    validations = {
        "created_at": {},
        "months": {
            "inclusive_maximum": 36,
        },
        "status_updated_at": {},
        "updated_at": {},
    }

    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "client_id": (str,),
            "created_at": (str,),
            "dataset_type": (str,),
            "error_messages": ([str],),
            "export_name": (str,),
            "export_path": (str,),
            "id": (int,),
            "months": (int,),
            "scope": (str,),
            "status": (str,),
            "status_updated_at": (str,),
            "storage_account": (str,),
            "storage_container": (str,),
            "updated_at": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "client_id": "client_id",
        "created_at": "created_at",
        "dataset_type": "dataset_type",
        "error_messages": "error_messages",
        "export_name": "export_name",
        "export_path": "export_path",
        "id": "id",
        "months": "months",
        "scope": "scope",
        "status": "status",
        "status_updated_at": "status_updated_at",
        "storage_account": "storage_account",
        "storage_container": "storage_container",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        account_id: str,
        client_id: str,
        dataset_type: str,
        export_name: str,
        export_path: str,
        scope: str,
        status: str,
        storage_account: str,
        storage_container: str,
        created_at: Union[str, UnsetType] = unset,
        error_messages: Union[List[str], UnsetType] = unset,
        id: Union[int, UnsetType] = unset,
        months: Union[int, UnsetType] = unset,
        status_updated_at: Union[str, UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Azure config.

        :param account_id: The tenant ID of the azure account.
        :type account_id: str

        :param client_id: The client ID of the Azure account.
        :type client_id: str

        :param created_at: The timestamp when the Azure config was created.
        :type created_at: str, optional

        :param dataset_type: The dataset type of the Azure config.
        :type dataset_type: str

        :param error_messages: The error messages for the Azure config.
        :type error_messages: [str], optional

        :param export_name: The name of the configured Azure Export.
        :type export_name: str

        :param export_path: The path where the Azure Export is saved.
        :type export_path: str

        :param id: The ID of the Azure config.
        :type id: int, optional

        :param months: The number of months the report has been backfilled. **Deprecated**.
        :type months: int, optional

        :param scope: The scope of your observed subscription.
        :type scope: str

        :param status: The status of the Azure config.
        :type status: str

        :param status_updated_at: The timestamp when the Azure config status was last updated.
        :type status_updated_at: str, optional

        :param storage_account: The name of the storage account where the Azure Export is saved.
        :type storage_account: str

        :param storage_container: The name of the storage container where the Azure Export is saved.
        :type storage_container: str

        :param updated_at: The timestamp when the Azure config was last updated.
        :type updated_at: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if error_messages is not unset:
            kwargs["error_messages"] = error_messages
        if id is not unset:
            kwargs["id"] = id
        if months is not unset:
            kwargs["months"] = months
        if status_updated_at is not unset:
            kwargs["status_updated_at"] = status_updated_at
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.client_id = client_id
        self_.dataset_type = dataset_type
        self_.export_name = export_name
        self_.export_path = export_path
        self_.scope = scope
        self_.status = status
        self_.storage_account = storage_account
        self_.storage_container = storage_container
