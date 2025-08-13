# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GeomapWidgetDefinitionView(ModelNormal):
    validations = {
        "custom_extent": {
            "max_items": 4,
            "min_items": 4,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "custom_extent": ([float],),
            "focus": (str,),
        }

    attribute_map = {
        "custom_extent": "custom_extent",
        "focus": "focus",
    }

    def __init__(self_, focus: str, custom_extent: Union[List[float], UnsetType] = unset, **kwargs):
        """
        The view of the world that the map should render.

        :param custom_extent: A custom extent of the map defined by an array of four numbers in the order ``[minLongitude, minLatitude, maxLongitude, maxLatitude]``.
        :type custom_extent: [float], optional

        :param focus: The ISO code of a country, sub-division, or region to focus the map on. Or ``WORLD``. Mutually exclusive with ``custom_extent``.
        :type focus: str
        """
        if custom_extent is not unset:
            kwargs["custom_extent"] = custom_extent
        super().__init__(kwargs)

        self_.focus = focus
