# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TreemapRequestStylePalette(ModelSimple):
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
    SUCCESS: ClassVar["TreemapRequestStylePalette"]
    RED: ClassVar["TreemapRequestStylePalette"]
    GREEN: ClassVar["TreemapRequestStylePalette"]
    ORANGE: ClassVar["TreemapRequestStylePalette"]
    GRAY: ClassVar["TreemapRequestStylePalette"]
    DOG_CLASSIC: ClassVar["TreemapRequestStylePalette"]
    DOG_CLASSIC_AREA: ClassVar["TreemapRequestStylePalette"]
    DOG_CLASSIC_LINE: ClassVar["TreemapRequestStylePalette"]
    DOG_CLASSIC_BARS: ClassVar["TreemapRequestStylePalette"]
    DOG_HIGHLIGHT: ClassVar["TreemapRequestStylePalette"]
    MONITOR_STATE: ClassVar["TreemapRequestStylePalette"]
    YELLOW_TO_GREEN: ClassVar["TreemapRequestStylePalette"]
    GREEN_TO_ORANGE: ClassVar["TreemapRequestStylePalette"]
    HOSTMAP_BLUES: ClassVar["TreemapRequestStylePalette"]
    HOSTMAP_GREEN_RED: ClassVar["TreemapRequestStylePalette"]
    HOSTMAP_GREEN_ORANGE_RED: ClassVar["TreemapRequestStylePalette"]
    HOSTMAP_BLUE_RED: ClassVar["TreemapRequestStylePalette"]
    DARK_GREY: ClassVar["TreemapRequestStylePalette"]
    PRIDE: ClassVar["TreemapRequestStylePalette"]
    GNBU: ClassVar["TreemapRequestStylePalette"]
    YLORRD: ClassVar["TreemapRequestStylePalette"]
    PURPLES: ClassVar["TreemapRequestStylePalette"]
    BLUES: ClassVar["TreemapRequestStylePalette"]
    ORANGES: ClassVar["TreemapRequestStylePalette"]
    REDS: ClassVar["TreemapRequestStylePalette"]
    GREENS: ClassVar["TreemapRequestStylePalette"]
    GREYS: ClassVar["TreemapRequestStylePalette"]
    STATUS_ERRORS: ClassVar["TreemapRequestStylePalette"]
    STATUS_WARNINGS: ClassVar["TreemapRequestStylePalette"]
    STATUS_SUCCESSES: ClassVar["TreemapRequestStylePalette"]
    PLASMA: ClassVar["TreemapRequestStylePalette"]
    VIRIDIS: ClassVar["TreemapRequestStylePalette"]
    DOGCAT: ClassVar["TreemapRequestStylePalette"]
    DATADOG16: ClassVar["TreemapRequestStylePalette"]
    PA_CLASSIC_LINE: ClassVar["TreemapRequestStylePalette"]
    PA_CLASSIC_AREA: ClassVar["TreemapRequestStylePalette"]
    PA_CLASSIC_BARS: ClassVar["TreemapRequestStylePalette"]
    PA_DATADOG16: ClassVar["TreemapRequestStylePalette"]
    CLASSIC: ClassVar["TreemapRequestStylePalette"]
    COOL_HM: ClassVar["TreemapRequestStylePalette"]
    WARM_HM: ClassVar["TreemapRequestStylePalette"]
    YELLOW___GREEN: ClassVar["TreemapRequestStylePalette"]
    GREEN___ORANGE: ClassVar["TreemapRequestStylePalette"]
    GREEN___RED: ClassVar["TreemapRequestStylePalette"]
    GREEN___ORANGE___RED: ClassVar["TreemapRequestStylePalette"]
    BLUE___RED: ClassVar["TreemapRequestStylePalette"]
    GOOD___BAD: ClassVar["TreemapRequestStylePalette"]
    COOL: ClassVar["TreemapRequestStylePalette"]
    OCEAN: ClassVar["TreemapRequestStylePalette"]
    WARM: ClassVar["TreemapRequestStylePalette"]
    FIRE: ClassVar["TreemapRequestStylePalette"]
    WARN: ClassVar["TreemapRequestStylePalette"]
    PURPLE: ClassVar["TreemapRequestStylePalette"]
    GREY: ClassVar["TreemapRequestStylePalette"]
    BLUE: ClassVar["TreemapRequestStylePalette"]
    DD20: ClassVar["TreemapRequestStylePalette"]
    SEMANTIC: ClassVar["TreemapRequestStylePalette"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TreemapRequestStylePalette.SUCCESS = TreemapRequestStylePalette("success")
TreemapRequestStylePalette.RED = TreemapRequestStylePalette("red")
TreemapRequestStylePalette.GREEN = TreemapRequestStylePalette("green")
TreemapRequestStylePalette.ORANGE = TreemapRequestStylePalette("orange")
TreemapRequestStylePalette.GRAY = TreemapRequestStylePalette("gray")
TreemapRequestStylePalette.DOG_CLASSIC = TreemapRequestStylePalette("dog_classic")
TreemapRequestStylePalette.DOG_CLASSIC_AREA = TreemapRequestStylePalette("dog_classic_area")
TreemapRequestStylePalette.DOG_CLASSIC_LINE = TreemapRequestStylePalette("dog_classic_line")
TreemapRequestStylePalette.DOG_CLASSIC_BARS = TreemapRequestStylePalette("dog_classic_bars")
TreemapRequestStylePalette.DOG_HIGHLIGHT = TreemapRequestStylePalette("dog_highlight")
TreemapRequestStylePalette.MONITOR_STATE = TreemapRequestStylePalette("monitor_state")
TreemapRequestStylePalette.YELLOW_TO_GREEN = TreemapRequestStylePalette("yellow_to_green")
TreemapRequestStylePalette.GREEN_TO_ORANGE = TreemapRequestStylePalette("green_to_orange")
TreemapRequestStylePalette.HOSTMAP_BLUES = TreemapRequestStylePalette("hostmap_blues")
TreemapRequestStylePalette.HOSTMAP_GREEN_RED = TreemapRequestStylePalette("hostmap_green_red")
TreemapRequestStylePalette.HOSTMAP_GREEN_ORANGE_RED = TreemapRequestStylePalette("hostmap_green_orange_red")
TreemapRequestStylePalette.HOSTMAP_BLUE_RED = TreemapRequestStylePalette("hostmap_blue_red")
TreemapRequestStylePalette.DARK_GREY = TreemapRequestStylePalette("dark_grey")
TreemapRequestStylePalette.PRIDE = TreemapRequestStylePalette("pride")
TreemapRequestStylePalette.GNBU = TreemapRequestStylePalette("GnBu")
TreemapRequestStylePalette.YLORRD = TreemapRequestStylePalette("YlOrRd")
TreemapRequestStylePalette.PURPLES = TreemapRequestStylePalette("Purples")
TreemapRequestStylePalette.BLUES = TreemapRequestStylePalette("Blues")
TreemapRequestStylePalette.ORANGES = TreemapRequestStylePalette("Oranges")
TreemapRequestStylePalette.REDS = TreemapRequestStylePalette("Reds")
TreemapRequestStylePalette.GREENS = TreemapRequestStylePalette("Greens")
TreemapRequestStylePalette.GREYS = TreemapRequestStylePalette("Greys")
TreemapRequestStylePalette.STATUS_ERRORS = TreemapRequestStylePalette("status_errors")
TreemapRequestStylePalette.STATUS_WARNINGS = TreemapRequestStylePalette("status_warnings")
TreemapRequestStylePalette.STATUS_SUCCESSES = TreemapRequestStylePalette("status_successes")
TreemapRequestStylePalette.PLASMA = TreemapRequestStylePalette("Plasma")
TreemapRequestStylePalette.VIRIDIS = TreemapRequestStylePalette("Viridis")
TreemapRequestStylePalette.DOGCAT = TreemapRequestStylePalette("dogcat")
TreemapRequestStylePalette.DATADOG16 = TreemapRequestStylePalette("datadog16")
TreemapRequestStylePalette.PA_CLASSIC_LINE = TreemapRequestStylePalette("pa_classic_line")
TreemapRequestStylePalette.PA_CLASSIC_AREA = TreemapRequestStylePalette("pa_classic_area")
TreemapRequestStylePalette.PA_CLASSIC_BARS = TreemapRequestStylePalette("pa_classic_bars")
TreemapRequestStylePalette.PA_DATADOG16 = TreemapRequestStylePalette("pa_datadog16")
TreemapRequestStylePalette.CLASSIC = TreemapRequestStylePalette("classic")
TreemapRequestStylePalette.COOL_HM = TreemapRequestStylePalette("Cool_hm")
TreemapRequestStylePalette.WARM_HM = TreemapRequestStylePalette("Warm_hm")
TreemapRequestStylePalette.YELLOW___GREEN = TreemapRequestStylePalette("Yellow / Green")
TreemapRequestStylePalette.GREEN___ORANGE = TreemapRequestStylePalette("Green / Orange")
TreemapRequestStylePalette.GREEN___RED = TreemapRequestStylePalette("Green / Red")
TreemapRequestStylePalette.GREEN___ORANGE___RED = TreemapRequestStylePalette("Green / Orange / Red")
TreemapRequestStylePalette.BLUE___RED = TreemapRequestStylePalette("Blue / Red")
TreemapRequestStylePalette.GOOD___BAD = TreemapRequestStylePalette("Good - bad")
TreemapRequestStylePalette.COOL = TreemapRequestStylePalette("cool")
TreemapRequestStylePalette.OCEAN = TreemapRequestStylePalette("ocean")
TreemapRequestStylePalette.WARM = TreemapRequestStylePalette("warm")
TreemapRequestStylePalette.FIRE = TreemapRequestStylePalette("fire")
TreemapRequestStylePalette.WARN = TreemapRequestStylePalette("warn")
TreemapRequestStylePalette.PURPLE = TreemapRequestStylePalette("purple")
TreemapRequestStylePalette.GREY = TreemapRequestStylePalette("grey")
TreemapRequestStylePalette.BLUE = TreemapRequestStylePalette("blue")
TreemapRequestStylePalette.DD20 = TreemapRequestStylePalette("dd20")
TreemapRequestStylePalette.SEMANTIC = TreemapRequestStylePalette("semantic")
