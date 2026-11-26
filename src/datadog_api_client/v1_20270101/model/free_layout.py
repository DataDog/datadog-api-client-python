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


class FreeLayout(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

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
        x: float,
        y: float,
        height: Union[float, UnsetType] = unset,
        width: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param height: Test-only generated schema for the dashboard versioning proof of concept.
        :type height: float, optional

        :param width: Test-only generated schema for the dashboard versioning proof of concept.
        :type width: float, optional

        :param x: Test-only generated schema for the dashboard versioning proof of concept.
        :type x: float

        :param y: Test-only generated schema for the dashboard versioning proof of concept.
        :type y: float
        """
        if height is not unset:
            kwargs["height"] = height
        if width is not unset:
            kwargs["width"] = width
        super().__init__(kwargs)

        self_.x = x
        self_.y = y
