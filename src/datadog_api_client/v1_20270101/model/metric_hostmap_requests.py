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
    from datadog_api_client.v1_20270101.model.hostmap_tile_def_fill_request import HostmapTileDefFillRequest
    from datadog_api_client.v1_20270101.model.hostmap_tile_def_size_request import HostmapTileDefSizeRequest


class MetricHostmapRequests(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.hostmap_tile_def_fill_request import HostmapTileDefFillRequest
        from datadog_api_client.v1_20270101.model.hostmap_tile_def_size_request import HostmapTileDefSizeRequest

        return {
            "fill": (HostmapTileDefFillRequest,),
            "size": (HostmapTileDefSizeRequest,),
        }

    attribute_map = {
        "fill": "fill",
        "size": "size",
    }

    def __init__(
        self_,
        fill: Union[HostmapTileDefFillRequest, UnsetType] = unset,
        size: Union[HostmapTileDefSizeRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param fill: Test-only generated schema for the dashboard versioning proof of concept.
        :type fill: HostmapTileDefFillRequest, optional

        :param size: Test-only generated schema for the dashboard versioning proof of concept.
        :type size: HostmapTileDefSizeRequest, optional
        """
        if fill is not unset:
            kwargs["fill"] = fill
        if size is not unset:
            kwargs["size"] = size
        super().__init__(kwargs)
