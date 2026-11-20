# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HostmapStylePalette(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["success", "red", "green", "orange", "gray", "dog_classic", "dog_classic_area", "dog_classic_line", "dog_classic_bars", "dog_highlight", "monitor_state", "yellow_to_green", "green_to_orange", "hostmap_blues", "hostmap_green_red", "hostmap_green_orange_red", "hostmap_blue_red", "dark_grey", "pride", "GnBu", "YlOrRd", "Purples", "Blues", "Oranges", "Reds", "Greens", "Greys", "status_errors", "status_warnings", "status_successes", "Plasma", "Viridis", "dogcat", "datadog16", "pa_classic_line", "pa_classic_area", "pa_classic_bars", "pa_datadog16", "classic", "Cool_hm", "Warm_hm", "Yellow / Green", "Green / Orange", "Green / Red", "Green / Orange / Red", "Blue / Red", "Good - bad", "cool", "ocean", "warm", "fire", "warn", "purple", "grey", "blue", "dd20"].
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
    }
    SUCCESS: ClassVar["HostmapStylePalette"]
    RED: ClassVar["HostmapStylePalette"]
    GREEN: ClassVar["HostmapStylePalette"]
    ORANGE: ClassVar["HostmapStylePalette"]
    GRAY: ClassVar["HostmapStylePalette"]
    DOG_CLASSIC: ClassVar["HostmapStylePalette"]
    DOG_CLASSIC_AREA: ClassVar["HostmapStylePalette"]
    DOG_CLASSIC_LINE: ClassVar["HostmapStylePalette"]
    DOG_CLASSIC_BARS: ClassVar["HostmapStylePalette"]
    DOG_HIGHLIGHT: ClassVar["HostmapStylePalette"]
    MONITOR_STATE: ClassVar["HostmapStylePalette"]
    YELLOW_TO_GREEN: ClassVar["HostmapStylePalette"]
    GREEN_TO_ORANGE: ClassVar["HostmapStylePalette"]
    HOSTMAP_BLUES: ClassVar["HostmapStylePalette"]
    HOSTMAP_GREEN_RED: ClassVar["HostmapStylePalette"]
    HOSTMAP_GREEN_ORANGE_RED: ClassVar["HostmapStylePalette"]
    HOSTMAP_BLUE_RED: ClassVar["HostmapStylePalette"]
    DARK_GREY: ClassVar["HostmapStylePalette"]
    PRIDE: ClassVar["HostmapStylePalette"]
    GNBU: ClassVar["HostmapStylePalette"]
    YLORRD: ClassVar["HostmapStylePalette"]
    PURPLES: ClassVar["HostmapStylePalette"]
    BLUES: ClassVar["HostmapStylePalette"]
    ORANGES: ClassVar["HostmapStylePalette"]
    REDS: ClassVar["HostmapStylePalette"]
    GREENS: ClassVar["HostmapStylePalette"]
    GREYS: ClassVar["HostmapStylePalette"]
    STATUS_ERRORS: ClassVar["HostmapStylePalette"]
    STATUS_WARNINGS: ClassVar["HostmapStylePalette"]
    STATUS_SUCCESSES: ClassVar["HostmapStylePalette"]
    PLASMA: ClassVar["HostmapStylePalette"]
    VIRIDIS: ClassVar["HostmapStylePalette"]
    DOGCAT: ClassVar["HostmapStylePalette"]
    DATADOG16: ClassVar["HostmapStylePalette"]
    PA_CLASSIC_LINE: ClassVar["HostmapStylePalette"]
    PA_CLASSIC_AREA: ClassVar["HostmapStylePalette"]
    PA_CLASSIC_BARS: ClassVar["HostmapStylePalette"]
    PA_DATADOG16: ClassVar["HostmapStylePalette"]
    CLASSIC: ClassVar["HostmapStylePalette"]
    COOL_HM: ClassVar["HostmapStylePalette"]
    WARM_HM: ClassVar["HostmapStylePalette"]
    YELLOW___GREEN: ClassVar["HostmapStylePalette"]
    GREEN___ORANGE: ClassVar["HostmapStylePalette"]
    GREEN___RED: ClassVar["HostmapStylePalette"]
    GREEN___ORANGE___RED: ClassVar["HostmapStylePalette"]
    BLUE___RED: ClassVar["HostmapStylePalette"]
    GOOD___BAD: ClassVar["HostmapStylePalette"]
    COOL: ClassVar["HostmapStylePalette"]
    OCEAN: ClassVar["HostmapStylePalette"]
    WARM: ClassVar["HostmapStylePalette"]
    FIRE: ClassVar["HostmapStylePalette"]
    WARN: ClassVar["HostmapStylePalette"]
    PURPLE: ClassVar["HostmapStylePalette"]
    GREY: ClassVar["HostmapStylePalette"]
    BLUE: ClassVar["HostmapStylePalette"]
    DD20: ClassVar["HostmapStylePalette"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HostmapStylePalette.SUCCESS = HostmapStylePalette("success")
HostmapStylePalette.RED = HostmapStylePalette("red")
HostmapStylePalette.GREEN = HostmapStylePalette("green")
HostmapStylePalette.ORANGE = HostmapStylePalette("orange")
HostmapStylePalette.GRAY = HostmapStylePalette("gray")
HostmapStylePalette.DOG_CLASSIC = HostmapStylePalette("dog_classic")
HostmapStylePalette.DOG_CLASSIC_AREA = HostmapStylePalette("dog_classic_area")
HostmapStylePalette.DOG_CLASSIC_LINE = HostmapStylePalette("dog_classic_line")
HostmapStylePalette.DOG_CLASSIC_BARS = HostmapStylePalette("dog_classic_bars")
HostmapStylePalette.DOG_HIGHLIGHT = HostmapStylePalette("dog_highlight")
HostmapStylePalette.MONITOR_STATE = HostmapStylePalette("monitor_state")
HostmapStylePalette.YELLOW_TO_GREEN = HostmapStylePalette("yellow_to_green")
HostmapStylePalette.GREEN_TO_ORANGE = HostmapStylePalette("green_to_orange")
HostmapStylePalette.HOSTMAP_BLUES = HostmapStylePalette("hostmap_blues")
HostmapStylePalette.HOSTMAP_GREEN_RED = HostmapStylePalette("hostmap_green_red")
HostmapStylePalette.HOSTMAP_GREEN_ORANGE_RED = HostmapStylePalette("hostmap_green_orange_red")
HostmapStylePalette.HOSTMAP_BLUE_RED = HostmapStylePalette("hostmap_blue_red")
HostmapStylePalette.DARK_GREY = HostmapStylePalette("dark_grey")
HostmapStylePalette.PRIDE = HostmapStylePalette("pride")
HostmapStylePalette.GNBU = HostmapStylePalette("GnBu")
HostmapStylePalette.YLORRD = HostmapStylePalette("YlOrRd")
HostmapStylePalette.PURPLES = HostmapStylePalette("Purples")
HostmapStylePalette.BLUES = HostmapStylePalette("Blues")
HostmapStylePalette.ORANGES = HostmapStylePalette("Oranges")
HostmapStylePalette.REDS = HostmapStylePalette("Reds")
HostmapStylePalette.GREENS = HostmapStylePalette("Greens")
HostmapStylePalette.GREYS = HostmapStylePalette("Greys")
HostmapStylePalette.STATUS_ERRORS = HostmapStylePalette("status_errors")
HostmapStylePalette.STATUS_WARNINGS = HostmapStylePalette("status_warnings")
HostmapStylePalette.STATUS_SUCCESSES = HostmapStylePalette("status_successes")
HostmapStylePalette.PLASMA = HostmapStylePalette("Plasma")
HostmapStylePalette.VIRIDIS = HostmapStylePalette("Viridis")
HostmapStylePalette.DOGCAT = HostmapStylePalette("dogcat")
HostmapStylePalette.DATADOG16 = HostmapStylePalette("datadog16")
HostmapStylePalette.PA_CLASSIC_LINE = HostmapStylePalette("pa_classic_line")
HostmapStylePalette.PA_CLASSIC_AREA = HostmapStylePalette("pa_classic_area")
HostmapStylePalette.PA_CLASSIC_BARS = HostmapStylePalette("pa_classic_bars")
HostmapStylePalette.PA_DATADOG16 = HostmapStylePalette("pa_datadog16")
HostmapStylePalette.CLASSIC = HostmapStylePalette("classic")
HostmapStylePalette.COOL_HM = HostmapStylePalette("Cool_hm")
HostmapStylePalette.WARM_HM = HostmapStylePalette("Warm_hm")
HostmapStylePalette.YELLOW___GREEN = HostmapStylePalette("Yellow / Green")
HostmapStylePalette.GREEN___ORANGE = HostmapStylePalette("Green / Orange")
HostmapStylePalette.GREEN___RED = HostmapStylePalette("Green / Red")
HostmapStylePalette.GREEN___ORANGE___RED = HostmapStylePalette("Green / Orange / Red")
HostmapStylePalette.BLUE___RED = HostmapStylePalette("Blue / Red")
HostmapStylePalette.GOOD___BAD = HostmapStylePalette("Good - bad")
HostmapStylePalette.COOL = HostmapStylePalette("cool")
HostmapStylePalette.OCEAN = HostmapStylePalette("ocean")
HostmapStylePalette.WARM = HostmapStylePalette("warm")
HostmapStylePalette.FIRE = HostmapStylePalette("fire")
HostmapStylePalette.WARN = HostmapStylePalette("warn")
HostmapStylePalette.PURPLE = HostmapStylePalette("purple")
HostmapStylePalette.GREY = HostmapStylePalette("grey")
HostmapStylePalette.BLUE = HostmapStylePalette("blue")
HostmapStylePalette.DD20 = HostmapStylePalette("dd20")
