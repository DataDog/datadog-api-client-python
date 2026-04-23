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


class SyntheticsTestResultBounds(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "height": (int,),
            "width": (int,),
            "x": (int,),
            "y": (int,),
        }

    attribute_map = {
        "height": "height",
        "width": "width",
        "x": "x",
        "y": "y",
    }

    def __init__(
        self_,
        height: Union[int, UnsetType] = unset,
        width: Union[int, UnsetType] = unset,
        x: Union[int, UnsetType] = unset,
        y: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Bounding box of an element on the page.

        :param height: Height in pixels.
        :type height: int, optional

        :param width: Width in pixels.
        :type width: int, optional

        :param x: Horizontal position in pixels.
        :type x: int, optional

        :param y: Vertical position in pixels.
        :type y: int, optional
        """
        if height is not unset:
            kwargs["height"] = height
        if width is not unset:
            kwargs["width"] = width
        if x is not unset:
            kwargs["x"] = x
        if y is not unset:
            kwargs["y"] = y
        super().__init__(kwargs)
