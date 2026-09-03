# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WidgetCalendarAlignedSpanType(ModelSimple):
    """
    Calendar-aligned time span type.

    :param value: Must be one of ["daily", "weekly", "monthly", "yearly"].
    :type value: str
    """

    allowed_values = {
        "daily",
        "weekly",
        "monthly",
        "yearly",
    }
    DAILY: ClassVar["WidgetCalendarAlignedSpanType"]
    WEEKLY: ClassVar["WidgetCalendarAlignedSpanType"]
    MONTHLY: ClassVar["WidgetCalendarAlignedSpanType"]
    YEARLY: ClassVar["WidgetCalendarAlignedSpanType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetCalendarAlignedSpanType.DAILY = WidgetCalendarAlignedSpanType("daily")
WidgetCalendarAlignedSpanType.WEEKLY = WidgetCalendarAlignedSpanType("weekly")
WidgetCalendarAlignedSpanType.MONTHLY = WidgetCalendarAlignedSpanType("monthly")
WidgetCalendarAlignedSpanType.YEARLY = WidgetCalendarAlignedSpanType("yearly")
