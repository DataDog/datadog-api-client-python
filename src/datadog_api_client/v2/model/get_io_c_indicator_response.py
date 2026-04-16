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
    from datadog_api_client.v2.model.get_io_c_indicator_response_data import GetIoCIndicatorResponseData


class GetIoCIndicatorResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_io_c_indicator_response_data import GetIoCIndicatorResponseData

        return {
            "data": (GetIoCIndicatorResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[GetIoCIndicatorResponseData, UnsetType] = unset, **kwargs):
        """
        Response for the get indicator of compromise endpoint.

        :param data: IoC indicator response data object.
        :type data: GetIoCIndicatorResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
