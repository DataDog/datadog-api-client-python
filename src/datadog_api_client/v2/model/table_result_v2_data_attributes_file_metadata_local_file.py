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


class TableResultV2DataAttributesFileMetadataLocalFile(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "error_message": (str,),
            "error_row_count": (int,),
            "upload_id": (str,),
        }

    attribute_map = {
        "error_message": "error_message",
        "error_row_count": "error_row_count",
        "upload_id": "upload_id",
    }

    def __init__(
        self_,
        error_message: Union[str, UnsetType] = unset,
        error_row_count: Union[int, UnsetType] = unset,
        upload_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        File metadata for reference tables created by upload.

        :param error_message: The error message returned from the creation/update.
        :type error_message: str, optional

        :param error_row_count: The number of rows that failed to create/update.
        :type error_row_count: int, optional

        :param upload_id: The upload ID that was used to create/update the table.
        :type upload_id: str, optional
        """
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if error_row_count is not unset:
            kwargs["error_row_count"] = error_row_count
        if upload_id is not unset:
            kwargs["upload_id"] = upload_id
        super().__init__(kwargs)
