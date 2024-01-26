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
    from datadog_api_client.v2.model.create_open_api_response_data import CreateOpenAPIResponseData


class CreateOpenAPIResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_open_api_response_data import CreateOpenAPIResponseData

        return {
            "data": (CreateOpenAPIResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[CreateOpenAPIResponseData, UnsetType] = unset, **kwargs):
        """
        Response for ``CreateOpenAPI`` operation.

        :param data: Data envelope for ``CreateOpenAPIResponse``.
        :type data: CreateOpenAPIResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
