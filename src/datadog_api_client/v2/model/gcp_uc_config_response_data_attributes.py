# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.gcp_cud_metadata_config import GCPCudMetadataConfig


class GcpUcConfigResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_cud_metadata_config import GCPCudMetadataConfig

        return {
            "account_id": (str,),
            "bucket_name": (str,),
            "created_at": (str,),
            "cud_metadata_config": (GCPCudMetadataConfig,),
            "cud_metadata_error_codes": ([int],),
            "cud_metadata_state": (str,),
            "cud_metadata_status_updated_at": (str,),
            "dataset": (str,),
            "error_messages": ([str], none_type),
            "export_prefix": (str,),
            "export_project_name": (str,),
            "months": (int,),
            "project_id": (str,),
            "service_account": (str,),
            "status": (str,),
            "status_updated_at": (str,),
            "updated_at": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "bucket_name": "bucket_name",
        "created_at": "created_at",
        "cud_metadata_config": "cud_metadata_config",
        "cud_metadata_error_codes": "cud_metadata_error_codes",
        "cud_metadata_state": "cud_metadata_state",
        "cud_metadata_status_updated_at": "cud_metadata_status_updated_at",
        "dataset": "dataset",
        "error_messages": "error_messages",
        "export_prefix": "export_prefix",
        "export_project_name": "export_project_name",
        "months": "months",
        "project_id": "project_id",
        "service_account": "service_account",
        "status": "status",
        "status_updated_at": "status_updated_at",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        bucket_name: Union[str, UnsetType] = unset,
        created_at: Union[str, UnsetType] = unset,
        cud_metadata_config: Union[GCPCudMetadataConfig, UnsetType] = unset,
        cud_metadata_error_codes: Union[List[int], UnsetType] = unset,
        cud_metadata_state: Union[str, UnsetType] = unset,
        cud_metadata_status_updated_at: Union[str, UnsetType] = unset,
        dataset: Union[str, UnsetType] = unset,
        error_messages: Union[List[str], none_type, UnsetType] = unset,
        export_prefix: Union[str, UnsetType] = unset,
        export_project_name: Union[str, UnsetType] = unset,
        months: Union[int, UnsetType] = unset,
        project_id: Union[str, UnsetType] = unset,
        service_account: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        status_updated_at: Union[str, UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``GcpUcConfigResponseDataAttributes`` object.

        :param account_id: The ``attributes`` ``account_id``.
        :type account_id: str, optional

        :param bucket_name: The ``attributes`` ``bucket_name``.
        :type bucket_name: str, optional

        :param created_at: The ``attributes`` ``created_at``.
        :type created_at: str, optional

        :param cud_metadata_config: The BigQuery table the committed use discount (CUD) metadata is read from. Only returned when CUD metadata is configured for the account.
        :type cud_metadata_config: GCPCudMetadataConfig, optional

        :param cud_metadata_error_codes: The error codes reported for the committed use discount (CUD) metadata export. Only returned when CUD metadata is configured for the account.
        :type cud_metadata_error_codes: [int], optional

        :param cud_metadata_state: The state of the Google Cloud committed use discount (CUD) metadata export. Only returned when CUD metadata is configured for the account.
        :type cud_metadata_state: str, optional

        :param cud_metadata_status_updated_at: The timestamp when the committed use discount (CUD) metadata state was last updated. Only returned when CUD metadata is configured for the account.
        :type cud_metadata_status_updated_at: str, optional

        :param dataset: The ``attributes`` ``dataset``.
        :type dataset: str, optional

        :param error_messages: The ``attributes`` ``error_messages``.
        :type error_messages: [str], none_type, optional

        :param export_prefix: The ``attributes`` ``export_prefix``.
        :type export_prefix: str, optional

        :param export_project_name: The ``attributes`` ``export_project_name``.
        :type export_project_name: str, optional

        :param months: The ``attributes`` ``months``.
        :type months: int, optional

        :param project_id: The ``attributes`` ``project_id``.
        :type project_id: str, optional

        :param service_account: The ``attributes`` ``service_account``.
        :type service_account: str, optional

        :param status: The ``attributes`` ``status``.
        :type status: str, optional

        :param status_updated_at: The ``attributes`` ``status_updated_at``.
        :type status_updated_at: str, optional

        :param updated_at: The ``attributes`` ``updated_at``.
        :type updated_at: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if bucket_name is not unset:
            kwargs["bucket_name"] = bucket_name
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if cud_metadata_config is not unset:
            kwargs["cud_metadata_config"] = cud_metadata_config
        if cud_metadata_error_codes is not unset:
            kwargs["cud_metadata_error_codes"] = cud_metadata_error_codes
        if cud_metadata_state is not unset:
            kwargs["cud_metadata_state"] = cud_metadata_state
        if cud_metadata_status_updated_at is not unset:
            kwargs["cud_metadata_status_updated_at"] = cud_metadata_status_updated_at
        if dataset is not unset:
            kwargs["dataset"] = dataset
        if error_messages is not unset:
            kwargs["error_messages"] = error_messages
        if export_prefix is not unset:
            kwargs["export_prefix"] = export_prefix
        if export_project_name is not unset:
            kwargs["export_project_name"] = export_project_name
        if months is not unset:
            kwargs["months"] = months
        if project_id is not unset:
            kwargs["project_id"] = project_id
        if service_account is not unset:
            kwargs["service_account"] = service_account
        if status is not unset:
            kwargs["status"] = status
        if status_updated_at is not unset:
            kwargs["status_updated_at"] = status_updated_at
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)
