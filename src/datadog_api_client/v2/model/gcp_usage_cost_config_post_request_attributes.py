# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GCPUsageCostConfigPostRequestAttributes(ModelNormal):
    validations = {
        "months": {
            "inclusive_maximum": 36,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "bucket_name": (str,),
            "dataset": (str,),
            "export_prefix": (str,),
            "export_project_name": (str,),
            "is_enabled": (bool,),
            "months": (int,),
            "service_account": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "bucket_name": "bucket_name",
        "dataset": "dataset",
        "export_prefix": "export_prefix",
        "export_project_name": "export_project_name",
        "is_enabled": "is_enabled",
        "months": "months",
        "service_account": "service_account",
    }

    def __init__(
        self_,
        account_id: str,
        bucket_name: str,
        dataset: str,
        export_prefix: str,
        export_project_name: str,
        service_account: str,
        is_enabled: Union[bool, UnsetType] = unset,
        months: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for GCP Usage Cost config post request.

        :param account_id: The GCP account ID.
        :type account_id: str

        :param bucket_name: The GCP bucket name used to store the Usage Cost export.
        :type bucket_name: str

        :param dataset: The export dataset name used for the GCP Usage Cost report.
        :type dataset: str

        :param export_prefix: The export prefix used for the GCP Usage Cost report.
        :type export_prefix: str

        :param export_project_name: The name of the GCP Usage Cost report.
        :type export_project_name: str

        :param is_enabled: Whether or not the Cloud Cost Management account is enabled.
        :type is_enabled: bool, optional

        :param months: The month of the report.
        :type months: int, optional

        :param service_account: The unique GCP service account email.
        :type service_account: str
        """
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if months is not unset:
            kwargs["months"] = months
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.bucket_name = bucket_name
        self_.dataset = dataset
        self_.export_prefix = export_prefix
        self_.export_project_name = export_project_name
        self_.service_account = service_account
