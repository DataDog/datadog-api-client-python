# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CalendarIntervalType(ModelSimple):
    """
    Type of calendar interval.

    :param value: Must be one of ["day", "week", "month", "year", "quarter", "minute", "hour"].
    :type value: str
    """

    allowed_values = {
        "day",
        "week",
        "month",
        "year",
        "quarter",
        "minute",
        "hour",
    }
    DAY: ClassVar["CalendarIntervalType"]
    WEEK: ClassVar["CalendarIntervalType"]
    MONTH: ClassVar["CalendarIntervalType"]
    YEAR: ClassVar["CalendarIntervalType"]
    QUARTER: ClassVar["CalendarIntervalType"]
    MINUTE: ClassVar["CalendarIntervalType"]
    HOUR: ClassVar["CalendarIntervalType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CalendarIntervalType.DAY = CalendarIntervalType("day")
CalendarIntervalType.WEEK = CalendarIntervalType("week")
CalendarIntervalType.MONTH = CalendarIntervalType("month")
CalendarIntervalType.YEAR = CalendarIntervalType("year")
CalendarIntervalType.QUARTER = CalendarIntervalType("quarter")
CalendarIntervalType.MINUTE = CalendarIntervalType("minute")
CalendarIntervalType.HOUR = CalendarIntervalType("hour")
