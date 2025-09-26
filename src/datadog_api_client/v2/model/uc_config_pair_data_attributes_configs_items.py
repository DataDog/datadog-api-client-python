# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class UCConfigPairDataAttributesConfigsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "client_id": (str,),
            "created_at": (str,),
            "dataset_type": (str,),
            "error_messages": ([str], none_type),
            "export_name": (str,),
            "export_path": (str,),
            "id": (str,),
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
        account_id: Union[str, UnsetType] = unset,
        client_id: Union[str, UnsetType] = unset,
        created_at: Union[str, UnsetType] = unset,
        dataset_type: Union[str, UnsetType] = unset,
        error_messages: Union[List[str], none_type, UnsetType] = unset,
        export_name: Union[str, UnsetType] = unset,
        export_path: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        months: Union[int, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        status_updated_at: Union[str, UnsetType] = unset,
        storage_account: Union[str, UnsetType] = unset,
        storage_container: Union[str, UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UCConfigPairDataAttributesConfigsItems`` object.

        :param account_id: The ``items`` ``account_id``.
        :type account_id: str, optional

        :param client_id: The ``items`` ``client_id``.
        :type client_id: str, optional

        :param created_at: The ``items`` ``created_at``.
        :type created_at: str, optional

        :param dataset_type: The ``items`` ``dataset_type``.
        :type dataset_type: str, optional

        :param error_messages: The ``items`` ``error_messages``.
        :type error_messages: [str], none_type, optional

        :param export_name: The ``items`` ``export_name``.
        :type export_name: str, optional

        :param export_path: The ``items`` ``export_path``.
        :type export_path: str, optional

        :param id: The ``items`` ``id``.
        :type id: str, optional

        :param months: The ``items`` ``months``.
        :type months: int, optional

        :param scope: The ``items`` ``scope``.
        :type scope: str, optional

        :param status: The ``items`` ``status``.
        :type status: str, optional

        :param status_updated_at: The ``items`` ``status_updated_at``.
        :type status_updated_at: str, optional

        :param storage_account: The ``items`` ``storage_account``.
        :type storage_account: str, optional

        :param storage_container: The ``items`` ``storage_container``.
        :type storage_container: str, optional

        :param updated_at: The ``items`` ``updated_at``.
        :type updated_at: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if client_id is not unset:
            kwargs["client_id"] = client_id
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if dataset_type is not unset:
            kwargs["dataset_type"] = dataset_type
        if error_messages is not unset:
            kwargs["error_messages"] = error_messages
        if export_name is not unset:
            kwargs["export_name"] = export_name
        if export_path is not unset:
            kwargs["export_path"] = export_path
        if id is not unset:
            kwargs["id"] = id
        if months is not unset:
            kwargs["months"] = months
        if scope is not unset:
            kwargs["scope"] = scope
        if status is not unset:
            kwargs["status"] = status
        if status_updated_at is not unset:
            kwargs["status_updated_at"] = status_updated_at
        if storage_account is not unset:
            kwargs["storage_account"] = storage_account
        if storage_container is not unset:
            kwargs["storage_container"] = storage_container
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)
