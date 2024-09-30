# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.devices_list_data import DevicesListData
    from datadog_api_client.v2.model.list_devices_response_metadata import ListDevicesResponseMetadata


class ListDevicesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.devices_list_data import DevicesListData
        from datadog_api_client.v2.model.list_devices_response_metadata import ListDevicesResponseMetadata

        return {
            "data": ([DevicesListData],),
            "meta": (ListDevicesResponseMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[DevicesListData], UnsetType] = unset,
        meta: Union[ListDevicesResponseMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        List devices response.

        :param data: The list devices response data.
        :type data: [DevicesListData], optional

        :param meta: Object describing meta attributes of response.
        :type meta: ListDevicesResponseMetadata, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
