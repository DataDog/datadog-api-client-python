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


class AnnotationDisplayBounds(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "height": (float,),
            "width": (float,),
            "x": (float,),
            "y": (float,),
        }

    attribute_map = {
        "height": "height",
        "width": "width",
        "x": "x",
        "y": "y",
    }

    def __init__(
        self_,
        height: Union[float, UnsetType] = unset,
        width: Union[float, UnsetType] = unset,
        x: Union[float, UnsetType] = unset,
        y: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AnnotationDisplayBounds`` object.

        :param height: The ``bounds`` ``height``.
        :type height: float, optional

        :param width: The ``bounds`` ``width``.
        :type width: float, optional

        :param x: The ``bounds`` ``x``.
        :type x: float, optional

        :param y: The ``bounds`` ``y``.
        :type y: float, optional
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
