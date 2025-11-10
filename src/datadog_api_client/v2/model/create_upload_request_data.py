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
    from datadog_api_client.v2.model.create_upload_request_data_attributes import CreateUploadRequestDataAttributes
    from datadog_api_client.v2.model.create_upload_request_data_type import CreateUploadRequestDataType


class CreateUploadRequestData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_upload_request_data_attributes import CreateUploadRequestDataAttributes
        from datadog_api_client.v2.model.create_upload_request_data_type import CreateUploadRequestDataType

        return {
            "attributes": (CreateUploadRequestDataAttributes,),
            "type": (CreateUploadRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: CreateUploadRequestDataType,
        attributes: Union[CreateUploadRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request data for creating an upload for a file to be ingested into a reference table.

        :param attributes: Upload configuration specifying how data is uploaded by the user, and properties of the table to associate the upload with.
        :type attributes: CreateUploadRequestDataAttributes, optional

        :param type: Upload resource type.
        :type type: CreateUploadRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
