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
    from datadog_api_client.v2.model.create_app_response_data_type import CreateAppResponseDataType


class CreateAppResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_app_response_data_type import CreateAppResponseDataType

        return {
            "id": (str,),
            "type": (CreateAppResponseDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: CreateAppResponseDataType, **kwargs):
        """
        The definition of ``CreateAppResponseData`` object.

        :param id: The ``data`` ``id``.
        :type id: str

        :param type: The definition of ``CreateAppResponseDataType`` object.
        :type type: CreateAppResponseDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
