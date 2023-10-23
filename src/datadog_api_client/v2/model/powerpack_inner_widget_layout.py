# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class PowerpackInnerWidgetLayout(ModelNormal):
    validations = {
        "height": {
            "inclusive_minimum": 0,
        },
        "width": {
            "inclusive_minimum": 0,
        },
        "x": {
            "inclusive_minimum": 0,
        },
        "y": {
            "inclusive_minimum": 0,
        },
    }

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

    def __init__(self_, height: int, width: int, x: int, y: int, **kwargs):
        """
        Powerpack inner widget layout.

        :param height: The height of the widget. Should be a non-negative integer.
        :type height: int

        :param width: The width of the widget. Should be a non-negative integer.
        :type width: int

        :param x: The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
        :type x: int

        :param y: The position of the widget on the y (vertical) axis. Should be a non-negative integer.
        :type y: int
        """
        super().__init__(kwargs)

        self_.height = height
        self_.width = width
        self_.x = x
        self_.y = y
