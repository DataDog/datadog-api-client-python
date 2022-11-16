# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardReportScheduleFrequency(ModelSimple):
    """
    Frequency with which to send the report.

    :param value: Must be one of ["1d", "2d", "3d", "4d", "5d", "6d", "1w", "2w", "3w", "1mo", "2mo", "3mo", "4mo", "5mo", "6mo", "7mo", "8mo", "9mo", "10mo", "11mo", "12mo"].
    :type value: str
    """

    allowed_values = {
        "1d",
        "2d",
        "3d",
        "4d",
        "5d",
        "6d",
        "1w",
        "2w",
        "3w",
        "1mo",
        "2mo",
        "3mo",
        "4mo",
        "5mo",
        "6mo",
        "7mo",
        "8mo",
        "9mo",
        "10mo",
        "11mo",
        "12mo",
    }
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_1D: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_2D: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_3D: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_4D: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_5D: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_6D: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_1W: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_2W: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_3W: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_1MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_2MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_3MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_4MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_5MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_6MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_7MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_8MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_9MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_10MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_11MO: ClassVar["DashboardReportScheduleFrequency"]
    DASHBOARD_REPORT_SCHEDULE_FREQUENCY_12MO: ClassVar["DashboardReportScheduleFrequency"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_1D = DashboardReportScheduleFrequency("1d")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_2D = DashboardReportScheduleFrequency("2d")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_3D = DashboardReportScheduleFrequency("3d")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_4D = DashboardReportScheduleFrequency("4d")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_5D = DashboardReportScheduleFrequency("5d")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_6D = DashboardReportScheduleFrequency("6d")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_1W = DashboardReportScheduleFrequency("1w")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_2W = DashboardReportScheduleFrequency("2w")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_3W = DashboardReportScheduleFrequency("3w")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_1MO = DashboardReportScheduleFrequency("1mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_2MO = DashboardReportScheduleFrequency("2mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_3MO = DashboardReportScheduleFrequency("3mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_4MO = DashboardReportScheduleFrequency("4mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_5MO = DashboardReportScheduleFrequency("5mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_6MO = DashboardReportScheduleFrequency("6mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_7MO = DashboardReportScheduleFrequency("7mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_8MO = DashboardReportScheduleFrequency("8mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_9MO = DashboardReportScheduleFrequency("9mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_10MO = DashboardReportScheduleFrequency("10mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_11MO = DashboardReportScheduleFrequency("11mo")
DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_12MO = DashboardReportScheduleFrequency("12mo")
