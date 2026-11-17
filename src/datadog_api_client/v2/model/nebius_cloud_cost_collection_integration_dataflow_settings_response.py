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


class NebiusCloudCostCollectionIntegrationDataflowSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "access_key_id": (str,),
            "bucket_name": (str,),
            "bucket_prefix_path": (str,),
            "bucket_region": (str,),
        }

    attribute_map = {
        "access_key_id": "access_key_id",
        "bucket_name": "bucket_name",
        "bucket_prefix_path": "bucket_prefix_path",
        "bucket_region": "bucket_region",
    }

    def __init__(
        self_,
        access_key_id: Union[str, UnsetType] = unset,
        bucket_name: Union[str, UnsetType] = unset,
        bucket_prefix_path: Union[str, UnsetType] = unset,
        bucket_region: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings of the Cloud Cost Management dataflow.

        :param access_key_id: ID of the Nebius Object Storage access key used to read the cost export bucket.
        :type access_key_id: str, optional

        :param bucket_name: Name of the Nebius Object Storage bucket holding the cost export.
        :type bucket_name: str, optional

        :param bucket_prefix_path: Prefix path within the bucket that locates the cost export.
        :type bucket_prefix_path: str, optional

        :param bucket_region: Region of the Nebius Object Storage bucket, such as ``eu-north1``.
        :type bucket_region: str, optional
        """
        if access_key_id is not unset:
            kwargs["access_key_id"] = access_key_id
        if bucket_name is not unset:
            kwargs["bucket_name"] = bucket_name
        if bucket_prefix_path is not unset:
            kwargs["bucket_prefix_path"] = bucket_prefix_path
        if bucket_region is not unset:
            kwargs["bucket_region"] = bucket_region
        super().__init__(kwargs)
