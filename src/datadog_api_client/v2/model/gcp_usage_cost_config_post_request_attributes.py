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
    @cached_property
    def openapi_types(_):
        return {
            "billing_account_id": (str,),
            "bucket_name": (str,),
            "export_dataset_name": (str,),
            "export_prefix": (str,),
            "export_project_name": (str,),
            "service_account": (str,),
        }

    attribute_map = {
        "billing_account_id": "billing_account_id",
        "bucket_name": "bucket_name",
        "export_dataset_name": "export_dataset_name",
        "export_prefix": "export_prefix",
        "export_project_name": "export_project_name",
        "service_account": "service_account",
    }

    def __init__(
        self_,
        billing_account_id: str,
        bucket_name: str,
        export_dataset_name: str,
        export_project_name: str,
        service_account: str,
        export_prefix: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for GCP Usage Cost config post request.

        :param billing_account_id: The GCP account ID.
        :type billing_account_id: str

        :param bucket_name: The GCP bucket name used to store the Usage Cost export.
        :type bucket_name: str

        :param export_dataset_name: The export dataset name used for the GCP Usage Cost report.
        :type export_dataset_name: str

        :param export_prefix: The export prefix used for the GCP Usage Cost report.
        :type export_prefix: str, optional

        :param export_project_name: The name of the GCP Usage Cost report.
        :type export_project_name: str

        :param service_account: The unique GCP service account email.
        :type service_account: str
        """
        if export_prefix is not unset:
            kwargs["export_prefix"] = export_prefix
        super().__init__(kwargs)

        self_.billing_account_id = billing_account_id
        self_.bucket_name = bucket_name
        self_.export_dataset_name = export_dataset_name
        self_.export_project_name = export_project_name
        self_.service_account = service_account
