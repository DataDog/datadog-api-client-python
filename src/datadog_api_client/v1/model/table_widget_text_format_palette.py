# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TableWidgetTextFormatPalette(ModelSimple):
    """
    Color-on-color palette to highlight replaced text.

    :param value: If omitted defaults to "white_on_green". Must be one of ["white_on_red", "white_on_yellow", "white_on_green", "black_on_light_red", "black_on_light_yellow", "black_on_light_green", "red_on_white", "yellow_on_white", "green_on_white", "custom_bg", "custom_text"].
    :type value: str
    """

    allowed_values = {
        "white_on_red",
        "white_on_yellow",
        "white_on_green",
        "black_on_light_red",
        "black_on_light_yellow",
        "black_on_light_green",
        "red_on_white",
        "yellow_on_white",
        "green_on_white",
        "custom_bg",
        "custom_text",
    }
    WHITE_ON_RED: ClassVar["TableWidgetTextFormatPalette"]
    WHITE_ON_YELLOW: ClassVar["TableWidgetTextFormatPalette"]
    WHITE_ON_GREEN: ClassVar["TableWidgetTextFormatPalette"]
    BLACK_ON_LIGHT_RED: ClassVar["TableWidgetTextFormatPalette"]
    BLACK_ON_LIGHT_YELLOW: ClassVar["TableWidgetTextFormatPalette"]
    BLACK_ON_LIGHT_GREEN: ClassVar["TableWidgetTextFormatPalette"]
    RED_ON_WHITE: ClassVar["TableWidgetTextFormatPalette"]
    YELLOW_ON_WHITE: ClassVar["TableWidgetTextFormatPalette"]
    GREEN_ON_WHITE: ClassVar["TableWidgetTextFormatPalette"]
    CUSTOM_BG: ClassVar["TableWidgetTextFormatPalette"]
    CUSTOM_TEXT: ClassVar["TableWidgetTextFormatPalette"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TableWidgetTextFormatPalette.WHITE_ON_RED = TableWidgetTextFormatPalette("white_on_red")
TableWidgetTextFormatPalette.WHITE_ON_YELLOW = TableWidgetTextFormatPalette("white_on_yellow")
TableWidgetTextFormatPalette.WHITE_ON_GREEN = TableWidgetTextFormatPalette("white_on_green")
TableWidgetTextFormatPalette.BLACK_ON_LIGHT_RED = TableWidgetTextFormatPalette("black_on_light_red")
TableWidgetTextFormatPalette.BLACK_ON_LIGHT_YELLOW = TableWidgetTextFormatPalette("black_on_light_yellow")
TableWidgetTextFormatPalette.BLACK_ON_LIGHT_GREEN = TableWidgetTextFormatPalette("black_on_light_green")
TableWidgetTextFormatPalette.RED_ON_WHITE = TableWidgetTextFormatPalette("red_on_white")
TableWidgetTextFormatPalette.YELLOW_ON_WHITE = TableWidgetTextFormatPalette("yellow_on_white")
TableWidgetTextFormatPalette.GREEN_ON_WHITE = TableWidgetTextFormatPalette("green_on_white")
TableWidgetTextFormatPalette.CUSTOM_BG = TableWidgetTextFormatPalette("custom_bg")
TableWidgetTextFormatPalette.CUSTOM_TEXT = TableWidgetTextFormatPalette("custom_text")
