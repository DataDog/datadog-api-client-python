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


class MSLBackendWidgetLayout(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "height": (float,),
            "is_column_break": (bool,),
            "width": (float,),
            "x": (float,),
            "y": (float,),
        }

    attribute_map = {
        "height": "height",
        "is_column_break": "is_column_break",
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
        is_column_break: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param height: Test-only generated schema for the dashboard versioning proof of concept.
        :type height: float

        :param is_column_break: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_column_break: bool, optional

        :param width: Test-only generated schema for the dashboard versioning proof of concept.
        :type width: float

        :param x: Test-only generated schema for the dashboard versioning proof of concept.
        :type x: float

        :param y: Test-only generated schema for the dashboard versioning proof of concept.
        :type y: float
        """
        if is_column_break is not unset:
            kwargs["is_column_break"] = is_column_break
        super().__init__(kwargs)

        self_.height = height
        self_.width = width
        self_.x = x
        self_.y = y
