# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SunburstRequestStylePalette(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["success", "red", "green", "orange", "gray", "dog_classic", "dog_classic_area", "dog_classic_line", "dog_classic_bars", "dog_highlight", "monitor_state", "yellow_to_green", "green_to_orange", "hostmap_blues", "hostmap_green_red", "hostmap_green_orange_red", "hostmap_blue_red", "dark_grey", "pride", "GnBu", "YlOrRd", "Purples", "Blues", "Oranges", "Reds", "Greens", "Greys", "status_errors", "status_warnings", "status_successes", "Plasma", "Viridis", "dogcat", "datadog16", "pa_classic_line", "pa_classic_area", "pa_classic_bars", "pa_datadog16", "classic", "Cool_hm", "Warm_hm", "Yellow / Green", "Green / Orange", "Green / Red", "Green / Orange / Red", "Blue / Red", "Good - bad", "cool", "ocean", "warm", "fire", "warn", "purple", "grey", "blue", "dd20", "semantic"].
    :type value: str
    """

    allowed_values = {
        "success",
        "red",
        "green",
        "orange",
        "gray",
        "dog_classic",
        "dog_classic_area",
        "dog_classic_line",
        "dog_classic_bars",
        "dog_highlight",
        "monitor_state",
        "yellow_to_green",
        "green_to_orange",
        "hostmap_blues",
        "hostmap_green_red",
        "hostmap_green_orange_red",
        "hostmap_blue_red",
        "dark_grey",
        "pride",
        "GnBu",
        "YlOrRd",
        "Purples",
        "Blues",
        "Oranges",
        "Reds",
        "Greens",
        "Greys",
        "status_errors",
        "status_warnings",
        "status_successes",
        "Plasma",
        "Viridis",
        "dogcat",
        "datadog16",
        "pa_classic_line",
        "pa_classic_area",
        "pa_classic_bars",
        "pa_datadog16",
        "classic",
        "Cool_hm",
        "Warm_hm",
        "Yellow / Green",
        "Green / Orange",
        "Green / Red",
        "Green / Orange / Red",
        "Blue / Red",
        "Good - bad",
        "cool",
        "ocean",
        "warm",
        "fire",
        "warn",
        "purple",
        "grey",
        "blue",
        "dd20",
        "semantic",
    }
    SUCCESS: ClassVar["SunburstRequestStylePalette"]
    RED: ClassVar["SunburstRequestStylePalette"]
    GREEN: ClassVar["SunburstRequestStylePalette"]
    ORANGE: ClassVar["SunburstRequestStylePalette"]
    GRAY: ClassVar["SunburstRequestStylePalette"]
    DOG_CLASSIC: ClassVar["SunburstRequestStylePalette"]
    DOG_CLASSIC_AREA: ClassVar["SunburstRequestStylePalette"]
    DOG_CLASSIC_LINE: ClassVar["SunburstRequestStylePalette"]
    DOG_CLASSIC_BARS: ClassVar["SunburstRequestStylePalette"]
    DOG_HIGHLIGHT: ClassVar["SunburstRequestStylePalette"]
    MONITOR_STATE: ClassVar["SunburstRequestStylePalette"]
    YELLOW_TO_GREEN: ClassVar["SunburstRequestStylePalette"]
    GREEN_TO_ORANGE: ClassVar["SunburstRequestStylePalette"]
    HOSTMAP_BLUES: ClassVar["SunburstRequestStylePalette"]
    HOSTMAP_GREEN_RED: ClassVar["SunburstRequestStylePalette"]
    HOSTMAP_GREEN_ORANGE_RED: ClassVar["SunburstRequestStylePalette"]
    HOSTMAP_BLUE_RED: ClassVar["SunburstRequestStylePalette"]
    DARK_GREY: ClassVar["SunburstRequestStylePalette"]
    PRIDE: ClassVar["SunburstRequestStylePalette"]
    GNBU: ClassVar["SunburstRequestStylePalette"]
    YLORRD: ClassVar["SunburstRequestStylePalette"]
    PURPLES: ClassVar["SunburstRequestStylePalette"]
    BLUES: ClassVar["SunburstRequestStylePalette"]
    ORANGES: ClassVar["SunburstRequestStylePalette"]
    REDS: ClassVar["SunburstRequestStylePalette"]
    GREENS: ClassVar["SunburstRequestStylePalette"]
    GREYS: ClassVar["SunburstRequestStylePalette"]
    STATUS_ERRORS: ClassVar["SunburstRequestStylePalette"]
    STATUS_WARNINGS: ClassVar["SunburstRequestStylePalette"]
    STATUS_SUCCESSES: ClassVar["SunburstRequestStylePalette"]
    PLASMA: ClassVar["SunburstRequestStylePalette"]
    VIRIDIS: ClassVar["SunburstRequestStylePalette"]
    DOGCAT: ClassVar["SunburstRequestStylePalette"]
    DATADOG16: ClassVar["SunburstRequestStylePalette"]
    PA_CLASSIC_LINE: ClassVar["SunburstRequestStylePalette"]
    PA_CLASSIC_AREA: ClassVar["SunburstRequestStylePalette"]
    PA_CLASSIC_BARS: ClassVar["SunburstRequestStylePalette"]
    PA_DATADOG16: ClassVar["SunburstRequestStylePalette"]
    CLASSIC: ClassVar["SunburstRequestStylePalette"]
    COOL_HM: ClassVar["SunburstRequestStylePalette"]
    WARM_HM: ClassVar["SunburstRequestStylePalette"]
    YELLOW___GREEN: ClassVar["SunburstRequestStylePalette"]
    GREEN___ORANGE: ClassVar["SunburstRequestStylePalette"]
    GREEN___RED: ClassVar["SunburstRequestStylePalette"]
    GREEN___ORANGE___RED: ClassVar["SunburstRequestStylePalette"]
    BLUE___RED: ClassVar["SunburstRequestStylePalette"]
    GOOD___BAD: ClassVar["SunburstRequestStylePalette"]
    COOL: ClassVar["SunburstRequestStylePalette"]
    OCEAN: ClassVar["SunburstRequestStylePalette"]
    WARM: ClassVar["SunburstRequestStylePalette"]
    FIRE: ClassVar["SunburstRequestStylePalette"]
    WARN: ClassVar["SunburstRequestStylePalette"]
    PURPLE: ClassVar["SunburstRequestStylePalette"]
    GREY: ClassVar["SunburstRequestStylePalette"]
    BLUE: ClassVar["SunburstRequestStylePalette"]
    DD20: ClassVar["SunburstRequestStylePalette"]
    SEMANTIC: ClassVar["SunburstRequestStylePalette"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SunburstRequestStylePalette.SUCCESS = SunburstRequestStylePalette("success")
SunburstRequestStylePalette.RED = SunburstRequestStylePalette("red")
SunburstRequestStylePalette.GREEN = SunburstRequestStylePalette("green")
SunburstRequestStylePalette.ORANGE = SunburstRequestStylePalette("orange")
SunburstRequestStylePalette.GRAY = SunburstRequestStylePalette("gray")
SunburstRequestStylePalette.DOG_CLASSIC = SunburstRequestStylePalette("dog_classic")
SunburstRequestStylePalette.DOG_CLASSIC_AREA = SunburstRequestStylePalette("dog_classic_area")
SunburstRequestStylePalette.DOG_CLASSIC_LINE = SunburstRequestStylePalette("dog_classic_line")
SunburstRequestStylePalette.DOG_CLASSIC_BARS = SunburstRequestStylePalette("dog_classic_bars")
SunburstRequestStylePalette.DOG_HIGHLIGHT = SunburstRequestStylePalette("dog_highlight")
SunburstRequestStylePalette.MONITOR_STATE = SunburstRequestStylePalette("monitor_state")
SunburstRequestStylePalette.YELLOW_TO_GREEN = SunburstRequestStylePalette("yellow_to_green")
SunburstRequestStylePalette.GREEN_TO_ORANGE = SunburstRequestStylePalette("green_to_orange")
SunburstRequestStylePalette.HOSTMAP_BLUES = SunburstRequestStylePalette("hostmap_blues")
SunburstRequestStylePalette.HOSTMAP_GREEN_RED = SunburstRequestStylePalette("hostmap_green_red")
SunburstRequestStylePalette.HOSTMAP_GREEN_ORANGE_RED = SunburstRequestStylePalette("hostmap_green_orange_red")
SunburstRequestStylePalette.HOSTMAP_BLUE_RED = SunburstRequestStylePalette("hostmap_blue_red")
SunburstRequestStylePalette.DARK_GREY = SunburstRequestStylePalette("dark_grey")
SunburstRequestStylePalette.PRIDE = SunburstRequestStylePalette("pride")
SunburstRequestStylePalette.GNBU = SunburstRequestStylePalette("GnBu")
SunburstRequestStylePalette.YLORRD = SunburstRequestStylePalette("YlOrRd")
SunburstRequestStylePalette.PURPLES = SunburstRequestStylePalette("Purples")
SunburstRequestStylePalette.BLUES = SunburstRequestStylePalette("Blues")
SunburstRequestStylePalette.ORANGES = SunburstRequestStylePalette("Oranges")
SunburstRequestStylePalette.REDS = SunburstRequestStylePalette("Reds")
SunburstRequestStylePalette.GREENS = SunburstRequestStylePalette("Greens")
SunburstRequestStylePalette.GREYS = SunburstRequestStylePalette("Greys")
SunburstRequestStylePalette.STATUS_ERRORS = SunburstRequestStylePalette("status_errors")
SunburstRequestStylePalette.STATUS_WARNINGS = SunburstRequestStylePalette("status_warnings")
SunburstRequestStylePalette.STATUS_SUCCESSES = SunburstRequestStylePalette("status_successes")
SunburstRequestStylePalette.PLASMA = SunburstRequestStylePalette("Plasma")
SunburstRequestStylePalette.VIRIDIS = SunburstRequestStylePalette("Viridis")
SunburstRequestStylePalette.DOGCAT = SunburstRequestStylePalette("dogcat")
SunburstRequestStylePalette.DATADOG16 = SunburstRequestStylePalette("datadog16")
SunburstRequestStylePalette.PA_CLASSIC_LINE = SunburstRequestStylePalette("pa_classic_line")
SunburstRequestStylePalette.PA_CLASSIC_AREA = SunburstRequestStylePalette("pa_classic_area")
SunburstRequestStylePalette.PA_CLASSIC_BARS = SunburstRequestStylePalette("pa_classic_bars")
SunburstRequestStylePalette.PA_DATADOG16 = SunburstRequestStylePalette("pa_datadog16")
SunburstRequestStylePalette.CLASSIC = SunburstRequestStylePalette("classic")
SunburstRequestStylePalette.COOL_HM = SunburstRequestStylePalette("Cool_hm")
SunburstRequestStylePalette.WARM_HM = SunburstRequestStylePalette("Warm_hm")
SunburstRequestStylePalette.YELLOW___GREEN = SunburstRequestStylePalette("Yellow / Green")
SunburstRequestStylePalette.GREEN___ORANGE = SunburstRequestStylePalette("Green / Orange")
SunburstRequestStylePalette.GREEN___RED = SunburstRequestStylePalette("Green / Red")
SunburstRequestStylePalette.GREEN___ORANGE___RED = SunburstRequestStylePalette("Green / Orange / Red")
SunburstRequestStylePalette.BLUE___RED = SunburstRequestStylePalette("Blue / Red")
SunburstRequestStylePalette.GOOD___BAD = SunburstRequestStylePalette("Good - bad")
SunburstRequestStylePalette.COOL = SunburstRequestStylePalette("cool")
SunburstRequestStylePalette.OCEAN = SunburstRequestStylePalette("ocean")
SunburstRequestStylePalette.WARM = SunburstRequestStylePalette("warm")
SunburstRequestStylePalette.FIRE = SunburstRequestStylePalette("fire")
SunburstRequestStylePalette.WARN = SunburstRequestStylePalette("warn")
SunburstRequestStylePalette.PURPLE = SunburstRequestStylePalette("purple")
SunburstRequestStylePalette.GREY = SunburstRequestStylePalette("grey")
SunburstRequestStylePalette.BLUE = SunburstRequestStylePalette("blue")
SunburstRequestStylePalette.DD20 = SunburstRequestStylePalette("dd20")
SunburstRequestStylePalette.SEMANTIC = SunburstRequestStylePalette("semantic")
