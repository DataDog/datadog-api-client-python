# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TableTrendType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["area", "line", "bars", "adjacent_bars"].
    :type value: str
    """

    allowed_values = {
        "area",
        "line",
        "bars",
        "adjacent_bars",
    }
    AREA: ClassVar["TableTrendType"]
    LINE: ClassVar["TableTrendType"]
    BARS: ClassVar["TableTrendType"]
    ADJACENT_BARS: ClassVar["TableTrendType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TableTrendType.AREA = TableTrendType("area")
TableTrendType.LINE = TableTrendType("line")
TableTrendType.BARS = TableTrendType("bars")
TableTrendType.ADJACENT_BARS = TableTrendType("adjacent_bars")
