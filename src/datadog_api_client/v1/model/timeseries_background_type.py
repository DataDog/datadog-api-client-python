# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class TimeseriesBackgroundType(StringEnum):
    """
    Timeseries is made using an area or bars.

    :param value: If omitted defaults to "area". Must be one of ["bars", "area"].
    :type value: str
    """

    allowed_values = {
        "bars",
        "area",
    }
    BARS: ClassVar["TimeseriesBackgroundType"]
    AREA: ClassVar["TimeseriesBackgroundType"]


TimeseriesBackgroundType.BARS = TimeseriesBackgroundType("bars")
TimeseriesBackgroundType.AREA = TimeseriesBackgroundType("area")
