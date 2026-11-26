# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HeatgridPresetName(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["dog_classic", "dog_classic_area", "dog_classic_line", "dog_classic_bars", "dog_highlight", "monitor_state", "yellow_to_green", "green_to_orange", "hostmap_blues", "hostmap_green_red", "hostmap_green_orange_red", "hostmap_blue_red", "dark_grey", "pride", "GnBu", "YlOrRd", "Purples", "Blues", "Oranges", "Reds", "Greens", "Greys", "status_errors", "status_warnings", "status_successes", "Plasma", "Viridis", "dogcat", "datadog16", "pa_classic_line", "pa_classic_area", "pa_classic_bars", "pa_datadog16", "classic"].
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
        "classic",
    }
    DOG_CLASSIC: ClassVar["HeatgridPresetName"]
    DOG_CLASSIC_AREA: ClassVar["HeatgridPresetName"]
    DOG_CLASSIC_LINE: ClassVar["HeatgridPresetName"]
    DOG_CLASSIC_BARS: ClassVar["HeatgridPresetName"]
    DOG_HIGHLIGHT: ClassVar["HeatgridPresetName"]
    MONITOR_STATE: ClassVar["HeatgridPresetName"]
    YELLOW_TO_GREEN: ClassVar["HeatgridPresetName"]
    GREEN_TO_ORANGE: ClassVar["HeatgridPresetName"]
    HOSTMAP_BLUES: ClassVar["HeatgridPresetName"]
    HOSTMAP_GREEN_RED: ClassVar["HeatgridPresetName"]
    HOSTMAP_GREEN_ORANGE_RED: ClassVar["HeatgridPresetName"]
    HOSTMAP_BLUE_RED: ClassVar["HeatgridPresetName"]
    DARK_GREY: ClassVar["HeatgridPresetName"]
    PRIDE: ClassVar["HeatgridPresetName"]
    GNBU: ClassVar["HeatgridPresetName"]
    YLORRD: ClassVar["HeatgridPresetName"]
    PURPLES: ClassVar["HeatgridPresetName"]
    BLUES: ClassVar["HeatgridPresetName"]
    ORANGES: ClassVar["HeatgridPresetName"]
    REDS: ClassVar["HeatgridPresetName"]
    GREENS: ClassVar["HeatgridPresetName"]
    GREYS: ClassVar["HeatgridPresetName"]
    STATUS_ERRORS: ClassVar["HeatgridPresetName"]
    STATUS_WARNINGS: ClassVar["HeatgridPresetName"]
    STATUS_SUCCESSES: ClassVar["HeatgridPresetName"]
    PLASMA: ClassVar["HeatgridPresetName"]
    VIRIDIS: ClassVar["HeatgridPresetName"]
    DOGCAT: ClassVar["HeatgridPresetName"]
    DATADOG16: ClassVar["HeatgridPresetName"]
    PA_CLASSIC_LINE: ClassVar["HeatgridPresetName"]
    PA_CLASSIC_AREA: ClassVar["HeatgridPresetName"]
    PA_CLASSIC_BARS: ClassVar["HeatgridPresetName"]
    PA_DATADOG16: ClassVar["HeatgridPresetName"]
    CLASSIC: ClassVar["HeatgridPresetName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HeatgridPresetName.DOG_CLASSIC = HeatgridPresetName("dog_classic")
HeatgridPresetName.DOG_CLASSIC_AREA = HeatgridPresetName("dog_classic_area")
HeatgridPresetName.DOG_CLASSIC_LINE = HeatgridPresetName("dog_classic_line")
HeatgridPresetName.DOG_CLASSIC_BARS = HeatgridPresetName("dog_classic_bars")
HeatgridPresetName.DOG_HIGHLIGHT = HeatgridPresetName("dog_highlight")
HeatgridPresetName.MONITOR_STATE = HeatgridPresetName("monitor_state")
HeatgridPresetName.YELLOW_TO_GREEN = HeatgridPresetName("yellow_to_green")
HeatgridPresetName.GREEN_TO_ORANGE = HeatgridPresetName("green_to_orange")
HeatgridPresetName.HOSTMAP_BLUES = HeatgridPresetName("hostmap_blues")
HeatgridPresetName.HOSTMAP_GREEN_RED = HeatgridPresetName("hostmap_green_red")
HeatgridPresetName.HOSTMAP_GREEN_ORANGE_RED = HeatgridPresetName("hostmap_green_orange_red")
HeatgridPresetName.HOSTMAP_BLUE_RED = HeatgridPresetName("hostmap_blue_red")
HeatgridPresetName.DARK_GREY = HeatgridPresetName("dark_grey")
HeatgridPresetName.PRIDE = HeatgridPresetName("pride")
HeatgridPresetName.GNBU = HeatgridPresetName("GnBu")
HeatgridPresetName.YLORRD = HeatgridPresetName("YlOrRd")
HeatgridPresetName.PURPLES = HeatgridPresetName("Purples")
HeatgridPresetName.BLUES = HeatgridPresetName("Blues")
HeatgridPresetName.ORANGES = HeatgridPresetName("Oranges")
HeatgridPresetName.REDS = HeatgridPresetName("Reds")
HeatgridPresetName.GREENS = HeatgridPresetName("Greens")
HeatgridPresetName.GREYS = HeatgridPresetName("Greys")
HeatgridPresetName.STATUS_ERRORS = HeatgridPresetName("status_errors")
HeatgridPresetName.STATUS_WARNINGS = HeatgridPresetName("status_warnings")
HeatgridPresetName.STATUS_SUCCESSES = HeatgridPresetName("status_successes")
HeatgridPresetName.PLASMA = HeatgridPresetName("Plasma")
HeatgridPresetName.VIRIDIS = HeatgridPresetName("Viridis")
HeatgridPresetName.DOGCAT = HeatgridPresetName("dogcat")
HeatgridPresetName.DATADOG16 = HeatgridPresetName("datadog16")
HeatgridPresetName.PA_CLASSIC_LINE = HeatgridPresetName("pa_classic_line")
HeatgridPresetName.PA_CLASSIC_AREA = HeatgridPresetName("pa_classic_area")
HeatgridPresetName.PA_CLASSIC_BARS = HeatgridPresetName("pa_classic_bars")
HeatgridPresetName.PA_DATADOG16 = HeatgridPresetName("pa_datadog16")
HeatgridPresetName.CLASSIC = HeatgridPresetName("classic")
