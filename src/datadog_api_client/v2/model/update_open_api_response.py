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
    from datadog_api_client.v2.model.update_open_api_response_data import UpdateOpenAPIResponseData


class UpdateOpenAPIResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_open_api_response_data import UpdateOpenAPIResponseData

        return {
            "data": (UpdateOpenAPIResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[UpdateOpenAPIResponseData, UnsetType] = unset, **kwargs):
        """
        Response for ``UpdateOpenAPI``.

        :param data: Data envelope for ``UpdateOpenAPIResponse``.
        :type data: UpdateOpenAPIResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
