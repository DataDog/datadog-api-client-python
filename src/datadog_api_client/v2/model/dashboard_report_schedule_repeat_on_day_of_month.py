# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardReportScheduleRepeatOnDayOfMonth(ModelSimple):
    """
    Defines which day of the month to send the monthly report. If the frequency field uses months (for example, `1mo`), this field is required. If the frequency field does not use months (for example `1d`, `1w`), then this field must be `null` (if provided). If this field is not provided in an update request, and the update request changes the frequency to use days or weeks (for example, `1d`, `1w`), then this field is automatically set to `null`. This field is mutually exclusive with `repeat_on_day_of_week`, and cannot be defined in the same request that includes a non-null value for `repeat_on_day_of_week`.

    :param value: Must be one of ["1st", "15th"].
    :type value: str
    """

    allowed_values = {
        "1st",
        "15th",
    }
    DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_MONTH_1ST: ClassVar["DashboardReportScheduleRepeatOnDayOfMonth"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_MONTH_15TH: ClassVar["DashboardReportScheduleRepeatOnDayOfMonth"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardReportScheduleRepeatOnDayOfMonth.DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_MONTH_1ST = (
    DashboardReportScheduleRepeatOnDayOfMonth("1st")
)
DashboardReportScheduleRepeatOnDayOfMonth.DASHBOARD_REPORT_SCHEDULE_REPEAT_ON_DAY_OF_MONTH_15TH = (
    DashboardReportScheduleRepeatOnDayOfMonth("15th")
)
