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
    from datadog_api_client.v2.model.get_device_data import GetDeviceData


class GetDeviceResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_device_data import GetDeviceData

        return {
            "data": (GetDeviceData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[GetDeviceData, UnsetType] = unset, **kwargs):
        """
        The ``GetDevice`` operation's response.

        :param data: Get device response data.
        :type data: GetDeviceData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
