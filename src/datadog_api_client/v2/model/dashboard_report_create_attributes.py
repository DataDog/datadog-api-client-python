# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dashboard_report_destination import DashboardReportDestination
    from datadog_api_client.v2.model.dashboard_report_schedule import DashboardReportSchedule
    from datadog_api_client.v2.model.dashboard_report_template_variables import DashboardReportTemplateVariables
    from datadog_api_client.v2.model.dashboard_report_timeframe import DashboardReportTimeframe


class DashboardReportCreateAttributes(ModelNormal):
    validations = {
        "description": {
            "max_length": 4096,
        },
        "title": {
            "max_length": 78,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report_destination import DashboardReportDestination
        from datadog_api_client.v2.model.dashboard_report_schedule import DashboardReportSchedule
        from datadog_api_client.v2.model.dashboard_report_template_variables import DashboardReportTemplateVariables
        from datadog_api_client.v2.model.dashboard_report_timeframe import DashboardReportTimeframe

        return {
            "description": (str, none_type),
            "destinations": (DashboardReportDestination,),
            "schedule": (DashboardReportSchedule,),
            "template_variables": (DashboardReportTemplateVariables,),
            "timeframe": (DashboardReportTimeframe,),
            "title": (str,),
        }

    attribute_map = {
        "description": "description",
        "destinations": "destinations",
        "schedule": "schedule",
        "template_variables": "template_variables",
        "timeframe": "timeframe",
        "title": "title",
    }

    def __init__(
        self_,
        destinations: DashboardReportDestination,
        schedule: DashboardReportSchedule,
        timeframe: DashboardReportTimeframe,
        title: str,
        description: Union[str, none_type, UnsetType] = unset,
        template_variables: Union[DashboardReportTemplateVariables, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for the dashboard report schema used to create a dashboard report.

        :param description: Description of the report in both the user interface and as part of the email body for each report sent. Must be a UTF-8 encoded string less than 4 KiB in size.
        :type description: str, none_type, optional

        :param destinations: Report destination-specific configuration. This determines how reports are sent. Only email destinations are supported.
        :type destinations: DashboardReportDestination

        :param schedule: Report schedule-specific configuration that defines when and how often a report is sent.
        :type schedule: DashboardReportSchedule

        :param template_variables: Template variables used to parameterize the dashboard when generating a report.
        :type template_variables: DashboardReportTemplateVariables, optional

        :param timeframe: Time period covered by the widgets in the dashboard report, at the time of report generation.
        :type timeframe: DashboardReportTimeframe

        :param title: Title of the report in both the user interface, and as part of the email subject for each report sent.
        :type title: str
        """
        if description is not unset:
            kwargs["description"] = description
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        super().__init__(kwargs)

        self_.destinations = destinations
        self_.schedule = schedule
        self_.timeframe = timeframe
        self_.title = title
