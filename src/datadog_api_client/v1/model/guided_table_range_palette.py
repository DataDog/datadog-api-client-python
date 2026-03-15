# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GuidedTableRangePalette(ModelSimple):
    """
    Color palette used by range-based conditional formatting rules.

    :param value: Must be one of ["transparent_to_green", "transparent_to_orange", "transparent_to_red", "transparent_to_blue", "red_transparent_green", "red_transparent_blue", "vivid_transparent_to_green", "vivid_transparent_to_orange", "vivid_transparent_to_red", "vivid_transparent_to_blue", "vivid_red_transparent_green", "vivid_red_transparent_blue"].
    :type value: str
    """

    allowed_values = {
        "transparent_to_green",
        "transparent_to_orange",
        "transparent_to_red",
        "transparent_to_blue",
        "red_transparent_green",
        "red_transparent_blue",
        "vivid_transparent_to_green",
        "vivid_transparent_to_orange",
        "vivid_transparent_to_red",
        "vivid_transparent_to_blue",
        "vivid_red_transparent_green",
        "vivid_red_transparent_blue",
    }
    TRANSPARENT_TO_GREEN: ClassVar["GuidedTableRangePalette"]
    TRANSPARENT_TO_ORANGE: ClassVar["GuidedTableRangePalette"]
    TRANSPARENT_TO_RED: ClassVar["GuidedTableRangePalette"]
    TRANSPARENT_TO_BLUE: ClassVar["GuidedTableRangePalette"]
    RED_TRANSPARENT_GREEN: ClassVar["GuidedTableRangePalette"]
    RED_TRANSPARENT_BLUE: ClassVar["GuidedTableRangePalette"]
    VIVID_TRANSPARENT_TO_GREEN: ClassVar["GuidedTableRangePalette"]
    VIVID_TRANSPARENT_TO_ORANGE: ClassVar["GuidedTableRangePalette"]
    VIVID_TRANSPARENT_TO_RED: ClassVar["GuidedTableRangePalette"]
    VIVID_TRANSPARENT_TO_BLUE: ClassVar["GuidedTableRangePalette"]
    VIVID_RED_TRANSPARENT_GREEN: ClassVar["GuidedTableRangePalette"]
    VIVID_RED_TRANSPARENT_BLUE: ClassVar["GuidedTableRangePalette"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GuidedTableRangePalette.TRANSPARENT_TO_GREEN = GuidedTableRangePalette("transparent_to_green")
GuidedTableRangePalette.TRANSPARENT_TO_ORANGE = GuidedTableRangePalette("transparent_to_orange")
GuidedTableRangePalette.TRANSPARENT_TO_RED = GuidedTableRangePalette("transparent_to_red")
GuidedTableRangePalette.TRANSPARENT_TO_BLUE = GuidedTableRangePalette("transparent_to_blue")
GuidedTableRangePalette.RED_TRANSPARENT_GREEN = GuidedTableRangePalette("red_transparent_green")
GuidedTableRangePalette.RED_TRANSPARENT_BLUE = GuidedTableRangePalette("red_transparent_blue")
GuidedTableRangePalette.VIVID_TRANSPARENT_TO_GREEN = GuidedTableRangePalette("vivid_transparent_to_green")
GuidedTableRangePalette.VIVID_TRANSPARENT_TO_ORANGE = GuidedTableRangePalette("vivid_transparent_to_orange")
GuidedTableRangePalette.VIVID_TRANSPARENT_TO_RED = GuidedTableRangePalette("vivid_transparent_to_red")
GuidedTableRangePalette.VIVID_TRANSPARENT_TO_BLUE = GuidedTableRangePalette("vivid_transparent_to_blue")
GuidedTableRangePalette.VIVID_RED_TRANSPARENT_GREEN = GuidedTableRangePalette("vivid_red_transparent_green")
GuidedTableRangePalette.VIVID_RED_TRANSPARENT_BLUE = GuidedTableRangePalette("vivid_red_transparent_blue")
