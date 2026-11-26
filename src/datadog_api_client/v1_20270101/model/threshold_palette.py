# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ThresholdPalette(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["white_on_red", "black_on_light_red", "white_on_green", "black_on_light_green", "white_on_yellow", "black_on_light_yellow", "white_on_gray", "green_on_white", "yellow_on_white", "red_on_white", "gray_on_white", "red", "green", "orange", "gray"].
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
    }
    WHITE_ON_RED: ClassVar["ThresholdPalette"]
    BLACK_ON_LIGHT_RED: ClassVar["ThresholdPalette"]
    WHITE_ON_GREEN: ClassVar["ThresholdPalette"]
    BLACK_ON_LIGHT_GREEN: ClassVar["ThresholdPalette"]
    WHITE_ON_YELLOW: ClassVar["ThresholdPalette"]
    BLACK_ON_LIGHT_YELLOW: ClassVar["ThresholdPalette"]
    WHITE_ON_GRAY: ClassVar["ThresholdPalette"]
    GREEN_ON_WHITE: ClassVar["ThresholdPalette"]
    YELLOW_ON_WHITE: ClassVar["ThresholdPalette"]
    RED_ON_WHITE: ClassVar["ThresholdPalette"]
    GRAY_ON_WHITE: ClassVar["ThresholdPalette"]
    RED: ClassVar["ThresholdPalette"]
    GREEN: ClassVar["ThresholdPalette"]
    ORANGE: ClassVar["ThresholdPalette"]
    GRAY: ClassVar["ThresholdPalette"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ThresholdPalette.WHITE_ON_RED = ThresholdPalette("white_on_red")
ThresholdPalette.BLACK_ON_LIGHT_RED = ThresholdPalette("black_on_light_red")
ThresholdPalette.WHITE_ON_GREEN = ThresholdPalette("white_on_green")
ThresholdPalette.BLACK_ON_LIGHT_GREEN = ThresholdPalette("black_on_light_green")
ThresholdPalette.WHITE_ON_YELLOW = ThresholdPalette("white_on_yellow")
ThresholdPalette.BLACK_ON_LIGHT_YELLOW = ThresholdPalette("black_on_light_yellow")
ThresholdPalette.WHITE_ON_GRAY = ThresholdPalette("white_on_gray")
ThresholdPalette.GREEN_ON_WHITE = ThresholdPalette("green_on_white")
ThresholdPalette.YELLOW_ON_WHITE = ThresholdPalette("yellow_on_white")
ThresholdPalette.RED_ON_WHITE = ThresholdPalette("red_on_white")
ThresholdPalette.GRAY_ON_WHITE = ThresholdPalette("gray_on_white")
ThresholdPalette.RED = ThresholdPalette("red")
ThresholdPalette.GREEN = ThresholdPalette("green")
ThresholdPalette.ORANGE = ThresholdPalette("orange")
ThresholdPalette.GRAY = ThresholdPalette("gray")
