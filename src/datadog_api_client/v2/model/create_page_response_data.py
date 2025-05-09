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
    from datadog_api_client.v2.model.create_page_response_data_type import CreatePageResponseDataType


class CreatePageResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_page_response_data_type import CreatePageResponseDataType

        return {
            "id": (str,),
            "type": (CreatePageResponseDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, type: CreatePageResponseDataType, id: Union[str, UnsetType] = unset, **kwargs):
        """
        The information returned after successfully creating a page.

        :param id: The unique ID of the created page.
        :type id: str, optional

        :param type: The type of resource used when creating an On-Call Page.
        :type type: CreatePageResponseDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
