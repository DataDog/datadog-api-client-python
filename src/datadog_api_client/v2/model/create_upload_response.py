# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_upload_response_data import CreateUploadResponseData


class CreateUploadResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_upload_response_data import CreateUploadResponseData

        return {
            "data": (CreateUploadResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[CreateUploadResponseData, UnsetType] = unset, **kwargs):
        """
        Information about the upload created containing the upload ID and pre-signed URLs to PUT chunks of the CSV file to.

        :param data: Upload ID and attributes of the created upload.
        :type data: CreateUploadResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
