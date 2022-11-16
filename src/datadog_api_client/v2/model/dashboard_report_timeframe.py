# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardReportTimeframe(ModelSimple):
    """
    Time period covered by the widgets in the dashboard report, at the time of report generation.

    :param value: Must be one of ["5m", "15m", "30m", "1h", "4h", "1d", "2d", "1w", "1mo"].
    :type value: str
    """

    allowed_values = {
        "5m",
        "15m",
        "30m",
        "1h",
        "4h",
        "1d",
        "2d",
        "1w",
        "1mo",
    }
    DASHBOARD_REPORT_TIMEFRAME_5M: ClassVar["DashboardReportTimeframe"]
    DASHBOARD_REPORT_TIMEFRAME_15M: ClassVar["DashboardReportTimeframe"]
    DASHBOARD_REPORT_TIMEFRAME_30M: ClassVar["DashboardReportTimeframe"]
    DASHBOARD_REPORT_TIMEFRAME_1H: ClassVar["DashboardReportTimeframe"]
    DASHBOARD_REPORT_TIMEFRAME_4H: ClassVar["DashboardReportTimeframe"]
    DASHBOARD_REPORT_TIMEFRAME_1D: ClassVar["DashboardReportTimeframe"]
    DASHBOARD_REPORT_TIMEFRAME_2D: ClassVar["DashboardReportTimeframe"]
    DASHBOARD_REPORT_TIMEFRAME_1W: ClassVar["DashboardReportTimeframe"]
    DASHBOARD_REPORT_TIMEFRAME_1MO: ClassVar["DashboardReportTimeframe"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardReportTimeframe.DASHBOARD_REPORT_TIMEFRAME_5M = DashboardReportTimeframe("5m")
DashboardReportTimeframe.DASHBOARD_REPORT_TIMEFRAME_15M = DashboardReportTimeframe("15m")
DashboardReportTimeframe.DASHBOARD_REPORT_TIMEFRAME_30M = DashboardReportTimeframe("30m")
DashboardReportTimeframe.DASHBOARD_REPORT_TIMEFRAME_1H = DashboardReportTimeframe("1h")
DashboardReportTimeframe.DASHBOARD_REPORT_TIMEFRAME_4H = DashboardReportTimeframe("4h")
DashboardReportTimeframe.DASHBOARD_REPORT_TIMEFRAME_1D = DashboardReportTimeframe("1d")
DashboardReportTimeframe.DASHBOARD_REPORT_TIMEFRAME_2D = DashboardReportTimeframe("2d")
DashboardReportTimeframe.DASHBOARD_REPORT_TIMEFRAME_1W = DashboardReportTimeframe("1w")
DashboardReportTimeframe.DASHBOARD_REPORT_TIMEFRAME_1MO = DashboardReportTimeframe("1mo")
