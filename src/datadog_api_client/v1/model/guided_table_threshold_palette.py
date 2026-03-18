# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GuidedTableThresholdPalette(ModelSimple):
    """
    Color palette used by threshold-based conditional formatting and text formatting rules in a guided table.

    :param value: Must be one of ["white_on_red", "black_on_light_red", "white_on_green", "black_on_light_green", "white_on_yellow", "black_on_light_yellow", "white_on_gray", "green_on_white", "yellow_on_white", "red_on_white", "gray_on_white", "red", "green", "orange", "gray", "custom_bg", "custom_text", "custom_image"].
    :type value: str
    """

    allowed_values = {
        "white_on_red",
        "black_on_light_red",
        "white_on_green",
        "black_on_light_green",
        "white_on_yellow",
        "black_on_light_yellow",
        "white_on_gray",
        "green_on_white",
        "yellow_on_white",
        "red_on_white",
        "gray_on_white",
        "red",
        "green",
        "orange",
        "gray",
        "custom_bg",
        "custom_text",
        "custom_image",
    }
    WHITE_ON_RED: ClassVar["GuidedTableThresholdPalette"]
    BLACK_ON_LIGHT_RED: ClassVar["GuidedTableThresholdPalette"]
    WHITE_ON_GREEN: ClassVar["GuidedTableThresholdPalette"]
    BLACK_ON_LIGHT_GREEN: ClassVar["GuidedTableThresholdPalette"]
    WHITE_ON_YELLOW: ClassVar["GuidedTableThresholdPalette"]
    BLACK_ON_LIGHT_YELLOW: ClassVar["GuidedTableThresholdPalette"]
    WHITE_ON_GRAY: ClassVar["GuidedTableThresholdPalette"]
    GREEN_ON_WHITE: ClassVar["GuidedTableThresholdPalette"]
    YELLOW_ON_WHITE: ClassVar["GuidedTableThresholdPalette"]
    RED_ON_WHITE: ClassVar["GuidedTableThresholdPalette"]
    GRAY_ON_WHITE: ClassVar["GuidedTableThresholdPalette"]
    RED: ClassVar["GuidedTableThresholdPalette"]
    GREEN: ClassVar["GuidedTableThresholdPalette"]
    ORANGE: ClassVar["GuidedTableThresholdPalette"]
    GRAY: ClassVar["GuidedTableThresholdPalette"]
    CUSTOM_BG: ClassVar["GuidedTableThresholdPalette"]
    CUSTOM_TEXT: ClassVar["GuidedTableThresholdPalette"]
    CUSTOM_IMAGE: ClassVar["GuidedTableThresholdPalette"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GuidedTableThresholdPalette.WHITE_ON_RED = GuidedTableThresholdPalette("white_on_red")
GuidedTableThresholdPalette.BLACK_ON_LIGHT_RED = GuidedTableThresholdPalette("black_on_light_red")
GuidedTableThresholdPalette.WHITE_ON_GREEN = GuidedTableThresholdPalette("white_on_green")
GuidedTableThresholdPalette.BLACK_ON_LIGHT_GREEN = GuidedTableThresholdPalette("black_on_light_green")
GuidedTableThresholdPalette.WHITE_ON_YELLOW = GuidedTableThresholdPalette("white_on_yellow")
GuidedTableThresholdPalette.BLACK_ON_LIGHT_YELLOW = GuidedTableThresholdPalette("black_on_light_yellow")
GuidedTableThresholdPalette.WHITE_ON_GRAY = GuidedTableThresholdPalette("white_on_gray")
GuidedTableThresholdPalette.GREEN_ON_WHITE = GuidedTableThresholdPalette("green_on_white")
GuidedTableThresholdPalette.YELLOW_ON_WHITE = GuidedTableThresholdPalette("yellow_on_white")
GuidedTableThresholdPalette.RED_ON_WHITE = GuidedTableThresholdPalette("red_on_white")
GuidedTableThresholdPalette.GRAY_ON_WHITE = GuidedTableThresholdPalette("gray_on_white")
GuidedTableThresholdPalette.RED = GuidedTableThresholdPalette("red")
GuidedTableThresholdPalette.GREEN = GuidedTableThresholdPalette("green")
GuidedTableThresholdPalette.ORANGE = GuidedTableThresholdPalette("orange")
GuidedTableThresholdPalette.GRAY = GuidedTableThresholdPalette("gray")
GuidedTableThresholdPalette.CUSTOM_BG = GuidedTableThresholdPalette("custom_bg")
GuidedTableThresholdPalette.CUSTOM_TEXT = GuidedTableThresholdPalette("custom_text")
GuidedTableThresholdPalette.CUSTOM_IMAGE = GuidedTableThresholdPalette("custom_image")
