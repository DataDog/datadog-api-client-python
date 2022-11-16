# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardReportScheduleRepeatAt(ModelSimple):
    """
    ISO8601 formatted time (HH:MM) to send the report, using the time zone specified in the `timezone` field.

    :param value: Must be one of ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"].
    :type value: str
    """

    allowed_values = {
        "00:00",
        "00:30",
        "01:00",
        "01:30",
        "02:00",
        "02:30",
        "03:00",
        "03:30",
        "04:00",
        "04:30",
        "05:00",
        "05:30",
        "06:00",
        "06:30",
        "07:00",
        "07:30",
        "08:00",
        "08:30",
        "09:00",
        "09:30",
        "10:00",
        "10:30",
        "11:00",
        "11:30",
        "12:00",
        "12:30",
        "13:00",
        "13:30",
        "14:00",
        "14:30",
        "15:00",
        "15:30",
        "16:00",
        "16:30",
        "17:00",
        "17:30",
        "18:00",
        "18:30",
        "19:00",
        "19:30",
        "20:00",
        "20:30",
        "21:00",
        "21:30",
        "22:00",
        "22:30",
        "23:00",
        "23:30",
    }
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_00_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_00_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_01_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_01_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_02_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_02_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_03_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_03_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_04_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_04_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_05_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_05_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_06_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_06_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_07_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_07_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_08_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_08_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_09_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_09_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_10_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_10_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_11_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_11_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_12_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_12_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_13_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_13_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_14_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_14_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_15_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_15_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_16_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_16_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_17_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_17_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_18_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_18_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_19_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_19_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_20_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_20_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_21_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_21_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_22_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_22_30: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_23_00: ClassVar["DashboardReportScheduleRepeatAt"]
    DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_23_30: ClassVar["DashboardReportScheduleRepeatAt"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_00_00 = DashboardReportScheduleRepeatAt("00:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_00_30 = DashboardReportScheduleRepeatAt("00:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_01_00 = DashboardReportScheduleRepeatAt("01:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_01_30 = DashboardReportScheduleRepeatAt("01:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_02_00 = DashboardReportScheduleRepeatAt("02:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_02_30 = DashboardReportScheduleRepeatAt("02:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_03_00 = DashboardReportScheduleRepeatAt("03:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_03_30 = DashboardReportScheduleRepeatAt("03:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_04_00 = DashboardReportScheduleRepeatAt("04:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_04_30 = DashboardReportScheduleRepeatAt("04:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_05_00 = DashboardReportScheduleRepeatAt("05:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_05_30 = DashboardReportScheduleRepeatAt("05:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_06_00 = DashboardReportScheduleRepeatAt("06:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_06_30 = DashboardReportScheduleRepeatAt("06:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_07_00 = DashboardReportScheduleRepeatAt("07:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_07_30 = DashboardReportScheduleRepeatAt("07:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_08_00 = DashboardReportScheduleRepeatAt("08:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_08_30 = DashboardReportScheduleRepeatAt("08:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_09_00 = DashboardReportScheduleRepeatAt("09:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_09_30 = DashboardReportScheduleRepeatAt("09:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_10_00 = DashboardReportScheduleRepeatAt("10:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_10_30 = DashboardReportScheduleRepeatAt("10:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_11_00 = DashboardReportScheduleRepeatAt("11:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_11_30 = DashboardReportScheduleRepeatAt("11:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_12_00 = DashboardReportScheduleRepeatAt("12:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_12_30 = DashboardReportScheduleRepeatAt("12:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_13_00 = DashboardReportScheduleRepeatAt("13:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_13_30 = DashboardReportScheduleRepeatAt("13:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_14_00 = DashboardReportScheduleRepeatAt("14:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_14_30 = DashboardReportScheduleRepeatAt("14:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_15_00 = DashboardReportScheduleRepeatAt("15:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_15_30 = DashboardReportScheduleRepeatAt("15:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_16_00 = DashboardReportScheduleRepeatAt("16:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_16_30 = DashboardReportScheduleRepeatAt("16:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_17_00 = DashboardReportScheduleRepeatAt("17:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_17_30 = DashboardReportScheduleRepeatAt("17:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_18_00 = DashboardReportScheduleRepeatAt("18:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_18_30 = DashboardReportScheduleRepeatAt("18:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_19_00 = DashboardReportScheduleRepeatAt("19:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_19_30 = DashboardReportScheduleRepeatAt("19:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_20_00 = DashboardReportScheduleRepeatAt("20:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_20_30 = DashboardReportScheduleRepeatAt("20:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_21_00 = DashboardReportScheduleRepeatAt("21:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_21_30 = DashboardReportScheduleRepeatAt("21:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_22_00 = DashboardReportScheduleRepeatAt("22:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_22_30 = DashboardReportScheduleRepeatAt("22:30")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_23_00 = DashboardReportScheduleRepeatAt("23:00")
DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_23_30 = DashboardReportScheduleRepeatAt("23:30")
