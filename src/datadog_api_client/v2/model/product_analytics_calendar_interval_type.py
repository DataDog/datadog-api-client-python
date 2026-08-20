# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsCalendarIntervalType(ModelSimple):
    """
    Calendar unit used to bucket cohorts.

    :param value: Must be one of ["minute", "hour", "day", "week", "month", "quarter", "year"].
    :type value: str
    """

    allowed_values = {
        "minute",
        "hour",
        "day",
        "week",
        "month",
        "quarter",
        "year",
    }
    MINUTE: ClassVar["ProductAnalyticsCalendarIntervalType"]
    HOUR: ClassVar["ProductAnalyticsCalendarIntervalType"]
    DAY: ClassVar["ProductAnalyticsCalendarIntervalType"]
    WEEK: ClassVar["ProductAnalyticsCalendarIntervalType"]
    MONTH: ClassVar["ProductAnalyticsCalendarIntervalType"]
    QUARTER: ClassVar["ProductAnalyticsCalendarIntervalType"]
    YEAR: ClassVar["ProductAnalyticsCalendarIntervalType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsCalendarIntervalType.MINUTE = ProductAnalyticsCalendarIntervalType("minute")
ProductAnalyticsCalendarIntervalType.HOUR = ProductAnalyticsCalendarIntervalType("hour")
ProductAnalyticsCalendarIntervalType.DAY = ProductAnalyticsCalendarIntervalType("day")
ProductAnalyticsCalendarIntervalType.WEEK = ProductAnalyticsCalendarIntervalType("week")
ProductAnalyticsCalendarIntervalType.MONTH = ProductAnalyticsCalendarIntervalType("month")
ProductAnalyticsCalendarIntervalType.QUARTER = ProductAnalyticsCalendarIntervalType("quarter")
ProductAnalyticsCalendarIntervalType.YEAR = ProductAnalyticsCalendarIntervalType("year")
