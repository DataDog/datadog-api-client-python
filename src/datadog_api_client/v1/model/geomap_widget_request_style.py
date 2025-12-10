# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GeomapWidgetRequestStyle(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "color_by": (str,),
        }

    attribute_map = {
        "color_by": "color_by",
    }

    def __init__(self_, color_by: Union[str, UnsetType] = unset, **kwargs):
        """
        The style to apply to the request for points layer.

        :param color_by: The category to color the points by.
        :type color_by: str, optional
        """
        if color_by is not unset:
            kwargs["color_by"] = color_by
        super().__init__(kwargs)
