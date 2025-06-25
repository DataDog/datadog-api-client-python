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


class GCPUsageCostConfigAttributes(ModelNormal):
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
            "bucket_name": (str,),
            "created_at": (str,),
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
        account_id: str,
        bucket_name: str,
        dataset: str,
        export_prefix: str,
        export_project_name: str,
        service_account: str,
        status: str,
        created_at: Union[str, UnsetType] = unset,
        error_messages: Union[List[str], none_type, UnsetType] = unset,
        months: Union[int, UnsetType] = unset,
        project_id: Union[str, UnsetType] = unset,
        status_updated_at: Union[str, UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a GCP Usage Cost config.

        :param account_id: The GCP account ID.
        :type account_id: str

        :param bucket_name: The GCP bucket name used to store the Usage Cost export.
        :type bucket_name: str

        :param created_at: The timestamp when the GCP Usage Cost config was created.
        :type created_at: str, optional

        :param dataset: The export dataset name used for the GCP Usage Cost Report.
        :type dataset: str

        :param error_messages: The error messages for the GCP Usage Cost config.
        :type error_messages: [str], none_type, optional

        :param export_prefix: The export prefix used for the GCP Usage Cost Report.
        :type export_prefix: str

        :param export_project_name: The name of the GCP Usage Cost Report.
        :type export_project_name: str

        :param months: The number of months the report has been backfilled. **Deprecated**.
        :type months: int, optional

        :param project_id: The ``project_id`` of the GCP Usage Cost report.
        :type project_id: str, optional

        :param service_account: The unique GCP service account email.
        :type service_account: str

        :param status: The status of the GCP Usage Cost config.
        :type status: str

        :param status_updated_at: The timestamp when the GCP Usage Cost config status was updated.
        :type status_updated_at: str, optional

        :param updated_at: The timestamp when the GCP Usage Cost config status was updated.
        :type updated_at: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if error_messages is not unset:
            kwargs["error_messages"] = error_messages
        if months is not unset:
            kwargs["months"] = months
        if project_id is not unset:
            kwargs["project_id"] = project_id
        if status_updated_at is not unset:
            kwargs["status_updated_at"] = status_updated_at
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.bucket_name = bucket_name
        self_.dataset = dataset
        self_.export_prefix = export_prefix
        self_.export_project_name = export_project_name
        self_.service_account = service_account
        self_.status = status
