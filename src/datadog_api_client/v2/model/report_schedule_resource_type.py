# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ReportScheduleResourceType(ModelSimple):
    """
    The type of dashboard resource the report schedule targets.

    :param value: Must be one of ["dashboard", "integration_dashboard"].
    :type value: str
    """

    allowed_values = {
        "dashboard",
        "integration_dashboard",
    }
    DASHBOARD: ClassVar["ReportScheduleResourceType"]
    INTEGRATION_DASHBOARD: ClassVar["ReportScheduleResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ReportScheduleResourceType.DASHBOARD = ReportScheduleResourceType("dashboard")
ReportScheduleResourceType.INTEGRATION_DASHBOARD = ReportScheduleResourceType("integration_dashboard")
