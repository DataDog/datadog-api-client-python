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


class TableResultV2DataAttributesFileMetadataOneOfAccessDetailsGcpDetail(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "file_path": (str,),
            "gcp_bucket_name": (str,),
            "gcp_project_id": (str,),
            "gcp_service_account_email": (str,),
        }

    attribute_map = {
        "file_path": "file_path",
        "gcp_bucket_name": "gcp_bucket_name",
        "gcp_project_id": "gcp_project_id",
        "gcp_service_account_email": "gcp_service_account_email",
    }

    def __init__(
        self_,
        file_path: Union[str, UnsetType] = unset,
        gcp_bucket_name: Union[str, UnsetType] = unset,
        gcp_project_id: Union[str, UnsetType] = unset,
        gcp_service_account_email: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Google Cloud Platform storage access configuration.

        :param file_path: The relative file path from the GCS bucket root to the CSV file.
        :type file_path: str, optional

        :param gcp_bucket_name: GCP bucket containing the CSV file.
        :type gcp_bucket_name: str, optional

        :param gcp_project_id: GCP project ID where the bucket is located.
        :type gcp_project_id: str, optional

        :param gcp_service_account_email: Service account email with read permissions for the GCS bucket.
        :type gcp_service_account_email: str, optional
        """
        if file_path is not unset:
            kwargs["file_path"] = file_path
        if gcp_bucket_name is not unset:
            kwargs["gcp_bucket_name"] = gcp_bucket_name
        if gcp_project_id is not unset:
            kwargs["gcp_project_id"] = gcp_project_id
        if gcp_service_account_email is not unset:
            kwargs["gcp_service_account_email"] = gcp_service_account_email
        super().__init__(kwargs)
