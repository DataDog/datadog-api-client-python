# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeSpan(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["1m", "5m", "10m", "15m", "30m", "1h", "4h", "1d", "2d", "1w", "1mo", "3mo", "6mo", "1y"].
    :type value: str
    """

    allowed_values = {
        "1m",
        "5m",
        "10m",
        "15m",
        "30m",
        "1h",
        "4h",
        "1d",
        "2d",
        "1w",
        "1mo",
        "3mo",
        "6mo",
        "1y",
    }
    ONE_M: ClassVar["TimeSpan"]
    FIVE_M: ClassVar["TimeSpan"]
    TEN_M: ClassVar["TimeSpan"]
    FIFTEEN_M: ClassVar["TimeSpan"]
    THIRTY_M: ClassVar["TimeSpan"]
    ONE_H: ClassVar["TimeSpan"]
    FOUR_H: ClassVar["TimeSpan"]
    ONE_D: ClassVar["TimeSpan"]
    TWO_D: ClassVar["TimeSpan"]
    ONE_W: ClassVar["TimeSpan"]
    ONE_MO: ClassVar["TimeSpan"]
    THREE_MO: ClassVar["TimeSpan"]
    SIX_MO: ClassVar["TimeSpan"]
    ONE_Y: ClassVar["TimeSpan"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeSpan.ONE_M = TimeSpan("1m")
TimeSpan.FIVE_M = TimeSpan("5m")
TimeSpan.TEN_M = TimeSpan("10m")
TimeSpan.FIFTEEN_M = TimeSpan("15m")
TimeSpan.THIRTY_M = TimeSpan("30m")
TimeSpan.ONE_H = TimeSpan("1h")
TimeSpan.FOUR_H = TimeSpan("4h")
TimeSpan.ONE_D = TimeSpan("1d")
TimeSpan.TWO_D = TimeSpan("2d")
TimeSpan.ONE_W = TimeSpan("1w")
TimeSpan.ONE_MO = TimeSpan("1mo")
TimeSpan.THREE_MO = TimeSpan("3mo")
TimeSpan.SIX_MO = TimeSpan("6mo")
TimeSpan.ONE_Y = TimeSpan("1y")
