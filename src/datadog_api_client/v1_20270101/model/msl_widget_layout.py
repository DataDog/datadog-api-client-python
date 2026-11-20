# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class MSLWidgetLayout(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "height": (float,),
            "parent": (float, none_type),
            "width": (float,),
            "x": (float,),
            "y": (float,),
        }

    attribute_map = {
        "height": "height",
        "parent": "parent",
        "width": "width",
        "x": "x",
        "y": "y",
    }

    def __init__(
        self_,
        height: float,
        width: float,
        x: float,
        y: float,
        parent: Union[float, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param height: Test-only generated schema for the dashboard versioning proof of concept.
        :type height: float

        :param parent: Test-only generated schema for the dashboard versioning proof of concept.
        :type parent: float, none_type, optional

        :param width: Test-only generated schema for the dashboard versioning proof of concept.
        :type width: float

        :param x: Test-only generated schema for the dashboard versioning proof of concept.
        :type x: float

        :param y: Test-only generated schema for the dashboard versioning proof of concept.
        :type y: float
        """
        if parent is not unset:
            kwargs["parent"] = parent
        super().__init__(kwargs)

        self_.height = height
        self_.width = width
        self_.x = x
        self_.y = y
