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


class SyntheticsTestResultDeviceResolution(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "height": (int,),
            "pixel_ratio": (float,),
            "width": (int,),
        }

    attribute_map = {
        "height": "height",
        "pixel_ratio": "pixel_ratio",
        "width": "width",
    }

    def __init__(
        self_,
        height: Union[int, UnsetType] = unset,
        pixel_ratio: Union[float, UnsetType] = unset,
        width: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Screen resolution of the device used to run the test.

        :param height: Viewport height in pixels.
        :type height: int, optional

        :param pixel_ratio: Device pixel ratio.
        :type pixel_ratio: float, optional

        :param width: Viewport width in pixels.
        :type width: int, optional
        """
        if height is not unset:
            kwargs["height"] = height
        if pixel_ratio is not unset:
            kwargs["pixel_ratio"] = pixel_ratio
        if width is not unset:
            kwargs["width"] = width
        super().__init__(kwargs)
