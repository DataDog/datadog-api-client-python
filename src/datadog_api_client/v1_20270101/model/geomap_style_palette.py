# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GeomapStylePalette(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["dog_classic", "dog_classic_area", "dog_classic_line", "dog_classic_bars", "dog_highlight", "monitor_state", "yellow_to_green", "green_to_orange", "hostmap_blues", "hostmap_green_red", "hostmap_green_orange_red", "hostmap_blue_red", "dark_grey", "pride", "GnBu", "YlOrRd", "Purples", "Blues", "Oranges", "Reds", "Greens", "Greys", "status_errors", "status_warnings", "status_successes", "Plasma", "Viridis", "dogcat", "datadog16", "pa_classic_line", "pa_classic_area", "pa_classic_bars", "pa_datadog16"].
    :type value: str
    """

    allowed_values = {
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
    }
    DOG_CLASSIC: ClassVar["GeomapStylePalette"]
    DOG_CLASSIC_AREA: ClassVar["GeomapStylePalette"]
    DOG_CLASSIC_LINE: ClassVar["GeomapStylePalette"]
    DOG_CLASSIC_BARS: ClassVar["GeomapStylePalette"]
    DOG_HIGHLIGHT: ClassVar["GeomapStylePalette"]
    MONITOR_STATE: ClassVar["GeomapStylePalette"]
    YELLOW_TO_GREEN: ClassVar["GeomapStylePalette"]
    GREEN_TO_ORANGE: ClassVar["GeomapStylePalette"]
    HOSTMAP_BLUES: ClassVar["GeomapStylePalette"]
    HOSTMAP_GREEN_RED: ClassVar["GeomapStylePalette"]
    HOSTMAP_GREEN_ORANGE_RED: ClassVar["GeomapStylePalette"]
    HOSTMAP_BLUE_RED: ClassVar["GeomapStylePalette"]
    DARK_GREY: ClassVar["GeomapStylePalette"]
    PRIDE: ClassVar["GeomapStylePalette"]
    GNBU: ClassVar["GeomapStylePalette"]
    YLORRD: ClassVar["GeomapStylePalette"]
    PURPLES: ClassVar["GeomapStylePalette"]
    BLUES: ClassVar["GeomapStylePalette"]
    ORANGES: ClassVar["GeomapStylePalette"]
    REDS: ClassVar["GeomapStylePalette"]
    GREENS: ClassVar["GeomapStylePalette"]
    GREYS: ClassVar["GeomapStylePalette"]
    STATUS_ERRORS: ClassVar["GeomapStylePalette"]
    STATUS_WARNINGS: ClassVar["GeomapStylePalette"]
    STATUS_SUCCESSES: ClassVar["GeomapStylePalette"]
    PLASMA: ClassVar["GeomapStylePalette"]
    VIRIDIS: ClassVar["GeomapStylePalette"]
    DOGCAT: ClassVar["GeomapStylePalette"]
    DATADOG16: ClassVar["GeomapStylePalette"]
    PA_CLASSIC_LINE: ClassVar["GeomapStylePalette"]
    PA_CLASSIC_AREA: ClassVar["GeomapStylePalette"]
    PA_CLASSIC_BARS: ClassVar["GeomapStylePalette"]
    PA_DATADOG16: ClassVar["GeomapStylePalette"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GeomapStylePalette.DOG_CLASSIC = GeomapStylePalette("dog_classic")
GeomapStylePalette.DOG_CLASSIC_AREA = GeomapStylePalette("dog_classic_area")
GeomapStylePalette.DOG_CLASSIC_LINE = GeomapStylePalette("dog_classic_line")
GeomapStylePalette.DOG_CLASSIC_BARS = GeomapStylePalette("dog_classic_bars")
GeomapStylePalette.DOG_HIGHLIGHT = GeomapStylePalette("dog_highlight")
GeomapStylePalette.MONITOR_STATE = GeomapStylePalette("monitor_state")
GeomapStylePalette.YELLOW_TO_GREEN = GeomapStylePalette("yellow_to_green")
GeomapStylePalette.GREEN_TO_ORANGE = GeomapStylePalette("green_to_orange")
GeomapStylePalette.HOSTMAP_BLUES = GeomapStylePalette("hostmap_blues")
GeomapStylePalette.HOSTMAP_GREEN_RED = GeomapStylePalette("hostmap_green_red")
GeomapStylePalette.HOSTMAP_GREEN_ORANGE_RED = GeomapStylePalette("hostmap_green_orange_red")
GeomapStylePalette.HOSTMAP_BLUE_RED = GeomapStylePalette("hostmap_blue_red")
GeomapStylePalette.DARK_GREY = GeomapStylePalette("dark_grey")
GeomapStylePalette.PRIDE = GeomapStylePalette("pride")
GeomapStylePalette.GNBU = GeomapStylePalette("GnBu")
GeomapStylePalette.YLORRD = GeomapStylePalette("YlOrRd")
GeomapStylePalette.PURPLES = GeomapStylePalette("Purples")
GeomapStylePalette.BLUES = GeomapStylePalette("Blues")
GeomapStylePalette.ORANGES = GeomapStylePalette("Oranges")
GeomapStylePalette.REDS = GeomapStylePalette("Reds")
GeomapStylePalette.GREENS = GeomapStylePalette("Greens")
GeomapStylePalette.GREYS = GeomapStylePalette("Greys")
GeomapStylePalette.STATUS_ERRORS = GeomapStylePalette("status_errors")
GeomapStylePalette.STATUS_WARNINGS = GeomapStylePalette("status_warnings")
GeomapStylePalette.STATUS_SUCCESSES = GeomapStylePalette("status_successes")
GeomapStylePalette.PLASMA = GeomapStylePalette("Plasma")
GeomapStylePalette.VIRIDIS = GeomapStylePalette("Viridis")
GeomapStylePalette.DOGCAT = GeomapStylePalette("dogcat")
GeomapStylePalette.DATADOG16 = GeomapStylePalette("datadog16")
GeomapStylePalette.PA_CLASSIC_LINE = GeomapStylePalette("pa_classic_line")
GeomapStylePalette.PA_CLASSIC_AREA = GeomapStylePalette("pa_classic_area")
GeomapStylePalette.PA_CLASSIC_BARS = GeomapStylePalette("pa_classic_bars")
GeomapStylePalette.PA_DATADOG16 = GeomapStylePalette("pa_datadog16")
