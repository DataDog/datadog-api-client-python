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
    from datadog_api_client.v2.model.list_tags_response_data import ListTagsResponseData


class ListTagsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_tags_response_data import ListTagsResponseData

        return {
            "data": (ListTagsResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[ListTagsResponseData, UnsetType] = unset, **kwargs):
        """
        List tags response.

        :param data: The list tags response data.
        :type data: ListTagsResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
