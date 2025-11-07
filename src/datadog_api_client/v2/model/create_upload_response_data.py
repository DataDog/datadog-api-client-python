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
    from datadog_api_client.v2.model.create_upload_response_data_attributes import CreateUploadResponseDataAttributes
    from datadog_api_client.v2.model.create_upload_response_data_type import CreateUploadResponseDataType


class CreateUploadResponseData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_upload_response_data_attributes import (
            CreateUploadResponseDataAttributes,
        )
        from datadog_api_client.v2.model.create_upload_response_data_type import CreateUploadResponseDataType

        return {
            "attributes": (CreateUploadResponseDataAttributes,),
            "id": (str,),
            "type": (CreateUploadResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: CreateUploadResponseDataType,
        attributes: Union[CreateUploadResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Upload ID and attributes of the created upload.

        :param attributes: Pre-signed URLs for uploading parts of the file.
        :type attributes: CreateUploadResponseDataAttributes, optional

        :param id: Unique identifier for this upload. Use this ID when creating the reference table.
        :type id: str, optional

        :param type: Upload resource type.
        :type type: CreateUploadResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
