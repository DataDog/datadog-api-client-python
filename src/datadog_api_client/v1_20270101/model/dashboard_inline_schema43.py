# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema43(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["global", "alert", "full_week", "full_month", "week_to_date", "month_to_date", "year_to_date"].
    :type value: str
    """

    allowed_values = {
        "global",
        "alert",
        "full_week",
        "full_month",
        "week_to_date",
        "month_to_date",
        "year_to_date",
    }
    GLOBAL: ClassVar["DashboardInlineSchema43"]
    ALERT: ClassVar["DashboardInlineSchema43"]
    FULL_WEEK: ClassVar["DashboardInlineSchema43"]
    FULL_MONTH: ClassVar["DashboardInlineSchema43"]
    WEEK_TO_DATE: ClassVar["DashboardInlineSchema43"]
    MONTH_TO_DATE: ClassVar["DashboardInlineSchema43"]
    YEAR_TO_DATE: ClassVar["DashboardInlineSchema43"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema43.GLOBAL = DashboardInlineSchema43("global")
DashboardInlineSchema43.ALERT = DashboardInlineSchema43("alert")
DashboardInlineSchema43.FULL_WEEK = DashboardInlineSchema43("full_week")
DashboardInlineSchema43.FULL_MONTH = DashboardInlineSchema43("full_month")
DashboardInlineSchema43.WEEK_TO_DATE = DashboardInlineSchema43("week_to_date")
DashboardInlineSchema43.MONTH_TO_DATE = DashboardInlineSchema43("month_to_date")
DashboardInlineSchema43.YEAR_TO_DATE = DashboardInlineSchema43("year_to_date")
