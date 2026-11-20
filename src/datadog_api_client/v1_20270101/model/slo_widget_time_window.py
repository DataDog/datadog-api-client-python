# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SloWidgetTimeWindow(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["week_to_date", "month_to_date", "7d", "30d", "90d", "previous_week", "previous_month", "global_time"].
    :type value: str
    """

    allowed_values = {
        "week_to_date",
        "month_to_date",
        "7d",
        "30d",
        "90d",
        "previous_week",
        "previous_month",
        "global_time",
    }
    WEEK_TO_DATE: ClassVar["SloWidgetTimeWindow"]
    MONTH_TO_DATE: ClassVar["SloWidgetTimeWindow"]
    SEVEN_D: ClassVar["SloWidgetTimeWindow"]
    THIRTY_D: ClassVar["SloWidgetTimeWindow"]
    NINETY_D: ClassVar["SloWidgetTimeWindow"]
    PREVIOUS_WEEK: ClassVar["SloWidgetTimeWindow"]
    PREVIOUS_MONTH: ClassVar["SloWidgetTimeWindow"]
    GLOBAL_TIME: ClassVar["SloWidgetTimeWindow"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SloWidgetTimeWindow.WEEK_TO_DATE = SloWidgetTimeWindow("week_to_date")
SloWidgetTimeWindow.MONTH_TO_DATE = SloWidgetTimeWindow("month_to_date")
SloWidgetTimeWindow.SEVEN_D = SloWidgetTimeWindow("7d")
SloWidgetTimeWindow.THIRTY_D = SloWidgetTimeWindow("30d")
SloWidgetTimeWindow.NINETY_D = SloWidgetTimeWindow("90d")
SloWidgetTimeWindow.PREVIOUS_WEEK = SloWidgetTimeWindow("previous_week")
SloWidgetTimeWindow.PREVIOUS_MONTH = SloWidgetTimeWindow("previous_month")
SloWidgetTimeWindow.GLOBAL_TIME = SloWidgetTimeWindow("global_time")
