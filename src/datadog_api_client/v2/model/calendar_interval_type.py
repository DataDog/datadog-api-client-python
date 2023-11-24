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
    Type of calendar interval (day, week, etc.).

    :param value: Must be one of ["day", "week", "month", "year"].
    :type value: str
    """

    allowed_values = {
        "day",
        "week",
        "month",
        "year",
    }
    day: ClassVar["CalendarIntervalType"]
    week: ClassVar["CalendarIntervalType"]
    month: ClassVar["CalendarIntervalType"]
    year: ClassVar["CalendarIntervalType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CalendarIntervalType.day = CalendarIntervalType("day")
CalendarIntervalType.week = CalendarIntervalType("week")
CalendarIntervalType.month = CalendarIntervalType("month")
CalendarIntervalType.year = CalendarIntervalType("year")
