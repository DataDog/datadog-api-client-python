# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.get_app_response_data_attributes import GetAppResponseDataAttributes
    from datadog_api_client.v2.model.get_app_response_data_type import GetAppResponseDataType


class GetAppResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_app_response_data_attributes import GetAppResponseDataAttributes
        from datadog_api_client.v2.model.get_app_response_data_type import GetAppResponseDataType

        return {
            "attributes": (GetAppResponseDataAttributes,),
            "id": (str,),
            "type": (GetAppResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: GetAppResponseDataAttributes, id: str, type: GetAppResponseDataType, **kwargs):
        """
        The definition of ``GetAppResponseData`` object.

        :param attributes: The definition of ``GetAppResponseDataAttributes`` object.
        :type attributes: GetAppResponseDataAttributes

        :param id: The ``data`` ``id``.
        :type id: str

        :param type: The definition of ``GetAppResponseDataType`` object.
        :type type: GetAppResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
