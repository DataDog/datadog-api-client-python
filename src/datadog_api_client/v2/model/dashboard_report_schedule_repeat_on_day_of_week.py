# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardReportScheduleRepeatOnDayOfWeek(ModelSimple):
    """
    Defines which day of the week to send the weekly report. If the frequency field uses weeks (such as `1w`), this field is required and defines which day of the week to send the report. If the frequency field does not use weeks (for example, `1d`, `1mo`), then this field must be `null` (if provided). If this field is not provided in an update request, and the update request changes the frequency to use days or months (for example, `1d`, `1mo`), then this field is automatically set to `null`.  This field is mutually exclusive with `repeat_on_day_of_month` and cannot be defined in the same request that includes a non-null value for `repeat_on_day_of_month`.

    :param value: Must be one of ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
    :type value: str
    """

    allowed_values = {
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    }
    DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_MONDAY: ClassVar["DashboardReportScheduleRepeatOnDayOfWeek"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_TUESDAY: ClassVar["DashboardReportScheduleRepeatOnDayOfWeek"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_WEDNESDAY: ClassVar["DashboardReportScheduleRepeatOnDayOfWeek"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_THURSDAY: ClassVar["DashboardReportScheduleRepeatOnDayOfWeek"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_FRIDAY: ClassVar["DashboardReportScheduleRepeatOnDayOfWeek"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_SATURDAY: ClassVar["DashboardReportScheduleRepeatOnDayOfWeek"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_SUNDAY: ClassVar["DashboardReportScheduleRepeatOnDayOfWeek"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardReportScheduleRepeatOnDayOfWeek.DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_MONDAY = (
    DashboardReportScheduleRepeatOnDayOfWeek("Monday")
)
DashboardReportScheduleRepeatOnDayOfWeek.DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_TUESDAY = (
    DashboardReportScheduleRepeatOnDayOfWeek("Tuesday")
)
DashboardReportScheduleRepeatOnDayOfWeek.DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_WEDNESDAY = (
    DashboardReportScheduleRepeatOnDayOfWeek("Wednesday")
)
DashboardReportScheduleRepeatOnDayOfWeek.DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_THURSDAY = (
    DashboardReportScheduleRepeatOnDayOfWeek("Thursday")
)
DashboardReportScheduleRepeatOnDayOfWeek.DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_FRIDAY = (
    DashboardReportScheduleRepeatOnDayOfWeek("Friday")
)
DashboardReportScheduleRepeatOnDayOfWeek.DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_SATURDAY = (
    DashboardReportScheduleRepeatOnDayOfWeek("Saturday")
)
DashboardReportScheduleRepeatOnDayOfWeek.DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_WEEK_SUNDAY = (
    DashboardReportScheduleRepeatOnDayOfWeek("Sunday")
)
