# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SunburstWidgetLegendTableType(StringEnum):
    """
    Whether or not to show a table legend.

    :param value: Must be one of ["table", "none"].
    :type value: str
    """

    allowed_values = {
        "table",
        "none",
    }
    TABLE: ClassVar["SunburstWidgetLegendTableType"]
    NONE: ClassVar["SunburstWidgetLegendTableType"]


SunburstWidgetLegendTableType.TABLE = SunburstWidgetLegendTableType("table")
SunburstWidgetLegendTableType.NONE = SunburstWidgetLegendTableType("none")
