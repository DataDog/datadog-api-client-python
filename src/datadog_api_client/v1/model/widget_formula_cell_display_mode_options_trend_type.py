# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WidgetFormulaCellDisplayModeOptionsTrendType(ModelSimple):
    """
    Trend type for the cell display mode options.

    :param value: Must be one of ["area", "line", "bars"].
    :type value: str
    """

    allowed_values = {
        "area",
        "line",
        "bars",
    }
    AREA: ClassVar["WidgetFormulaCellDisplayModeOptionsTrendType"]
    LINE: ClassVar["WidgetFormulaCellDisplayModeOptionsTrendType"]
    BARS: ClassVar["WidgetFormulaCellDisplayModeOptionsTrendType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetFormulaCellDisplayModeOptionsTrendType.AREA = WidgetFormulaCellDisplayModeOptionsTrendType("area")
WidgetFormulaCellDisplayModeOptionsTrendType.LINE = WidgetFormulaCellDisplayModeOptionsTrendType("line")
WidgetFormulaCellDisplayModeOptionsTrendType.BARS = WidgetFormulaCellDisplayModeOptionsTrendType("bars")
