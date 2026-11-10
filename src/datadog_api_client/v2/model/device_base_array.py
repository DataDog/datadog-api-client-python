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
    from datadog_api_client.v2.model.device_base_data import DeviceBaseData
    from datadog_api_client.v2.model.device_base_array_links import DeviceBaseArrayLinks
    from datadog_api_client.v2.model.device_base_array_meta import DeviceBaseArrayMeta


class DeviceBaseArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.device_base_data import DeviceBaseData
        from datadog_api_client.v2.model.device_base_array_links import DeviceBaseArrayLinks
        from datadog_api_client.v2.model.device_base_array_meta import DeviceBaseArrayMeta

        return {
            "data": ([DeviceBaseData],),
            "links": (DeviceBaseArrayLinks,),
            "meta": (DeviceBaseArrayMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[DeviceBaseData],
        links: Union[DeviceBaseArrayLinks, UnsetType] = unset,
        meta: Union[DeviceBaseArrayMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response body for the list devices endpoint.

        :param data: List of devices matching the request.
        :type data: [DeviceBaseData]

        :param links: Links related to the current page of devices.
        :type links: DeviceBaseArrayLinks, optional

        :param meta: Metadata about the list devices response.
        :type meta: DeviceBaseArrayMeta, optional
        """
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
