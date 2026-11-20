# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WidgetDisplayType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["overlay", "area", "line", "bars", "adjacent_bars"].
    :type value: str
    """

    allowed_values = {
        "overlay",
        "area",
        "line",
        "bars",
        "adjacent_bars",
    }
    OVERLAY: ClassVar["WidgetDisplayType"]
    AREA: ClassVar["WidgetDisplayType"]
    LINE: ClassVar["WidgetDisplayType"]
    BARS: ClassVar["WidgetDisplayType"]
    ADJACENT_BARS: ClassVar["WidgetDisplayType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetDisplayType.OVERLAY = WidgetDisplayType("overlay")
WidgetDisplayType.AREA = WidgetDisplayType("area")
WidgetDisplayType.LINE = WidgetDisplayType("line")
WidgetDisplayType.BARS = WidgetDisplayType("bars")
WidgetDisplayType.ADJACENT_BARS = WidgetDisplayType("adjacent_bars")
