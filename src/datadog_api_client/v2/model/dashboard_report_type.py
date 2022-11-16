# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardReportType(ModelSimple):
    """
    JSON:API type of the dashboard report.

    :param value: If omitted defaults to "dashboard_reports". Must be one of ["dashboard_reports"].
    :type value: str
    """

    allowed_values = {
        "dashboard_reports",
    }
    DASHBOARD_REPORTS_TYPE: ClassVar["DashboardReportType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardReportType.DASHBOARD_REPORTS_TYPE = DashboardReportType("dashboard_reports")
