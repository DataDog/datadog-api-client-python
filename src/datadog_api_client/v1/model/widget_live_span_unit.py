# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WidgetLiveSpanUnit(ModelSimple):
    """
    Unit of the time span.

    :param value: Must be one of ["minute", "hour", "day", "week", "month", "year"].
    :type value: str
    """

    allowed_values = {
        "minute",
        "hour",
        "day",
        "week",
        "month",
        "year",
    }
    MINUTE: ClassVar["WidgetLiveSpanUnit"]
    HOUR: ClassVar["WidgetLiveSpanUnit"]
    DAY: ClassVar["WidgetLiveSpanUnit"]
    WEEK: ClassVar["WidgetLiveSpanUnit"]
    MONTH: ClassVar["WidgetLiveSpanUnit"]
    YEAR: ClassVar["WidgetLiveSpanUnit"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetLiveSpanUnit.MINUTE = WidgetLiveSpanUnit("minute")
WidgetLiveSpanUnit.HOUR = WidgetLiveSpanUnit("hour")
WidgetLiveSpanUnit.DAY = WidgetLiveSpanUnit("day")
WidgetLiveSpanUnit.WEEK = WidgetLiveSpanUnit("week")
WidgetLiveSpanUnit.MONTH = WidgetLiveSpanUnit("month")
WidgetLiveSpanUnit.YEAR = WidgetLiveSpanUnit("year")
