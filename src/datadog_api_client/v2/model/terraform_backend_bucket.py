# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.terraform_backend_sync_status import TerraformBackendSyncStatus


class TerraformBackendBucket(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.terraform_backend_sync_status import TerraformBackendSyncStatus

        return {
            "bucket_name": (str,),
            "last_sync_error": (str,),
            "last_sync_status": (TerraformBackendSyncStatus,),
            "last_sync_time": (datetime, none_type),
            "recurring_blob_sync_id": (str,),
            "statefile_count": (int,),
        }

    attribute_map = {
        "bucket_name": "bucket_name",
        "last_sync_error": "last_sync_error",
        "last_sync_status": "last_sync_status",
        "last_sync_time": "last_sync_time",
        "recurring_blob_sync_id": "recurring_blob_sync_id",
        "statefile_count": "statefile_count",
    }

    def __init__(
        self_,
        bucket_name: str,
        last_sync_error: str,
        last_sync_status: TerraformBackendSyncStatus,
        last_sync_time: Union[datetime, none_type],
        recurring_blob_sync_id: str,
        statefile_count: int,
        **kwargs,
    ):
        """
        Synchronization status for an S3 bucket.

        :param bucket_name: Name of the source S3 bucket.
        :type bucket_name: str

        :param last_sync_error: Error from the most recent failed synchronization, or an empty string otherwise.
        :type last_sync_error: str

        :param last_sync_status: Most recent synchronization outcome, or pending if no outcome has been recorded.
        :type last_sync_status: TerraformBackendSyncStatus

        :param last_sync_time: Time of the most recent synchronization outcome, or null if none has been recorded.
        :type last_sync_time: datetime, none_type

        :param recurring_blob_sync_id: Identifier of the recurring synchronization job.
        :type recurring_blob_sync_id: str

        :param statefile_count: Number of synchronized Terraform state files in the bucket.
        :type statefile_count: int
        """
        super().__init__(kwargs)

        self_.bucket_name = bucket_name
        self_.last_sync_error = last_sync_error
        self_.last_sync_status = last_sync_status
        self_.last_sync_time = last_sync_time
        self_.recurring_blob_sync_id = recurring_blob_sync_id
        self_.statefile_count = statefile_count
