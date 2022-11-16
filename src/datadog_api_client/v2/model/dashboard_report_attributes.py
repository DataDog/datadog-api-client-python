# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dashboard_report_destination import DashboardReportDestination
    from datadog_api_client.v2.model.dashboard_report_schedule import DashboardReportSchedule
    from datadog_api_client.v2.model.dashboard_report_template_variables import DashboardReportTemplateVariables
    from datadog_api_client.v2.model.dashboard_report_timeframe import DashboardReportTimeframe


class DashboardReportAttributes(ModelNormal):
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
            "created_at": (datetime,),
            "description": (str, none_type),
            "destinations": (DashboardReportDestination,),
            "modified_at": (datetime, none_type),
            "schedule": (DashboardReportSchedule,),
            "template_variables": (DashboardReportTemplateVariables,),
            "timeframe": (DashboardReportTimeframe,),
            "title": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "destinations": "destinations",
        "modified_at": "modified_at",
        "schedule": "schedule",
        "template_variables": "template_variables",
        "timeframe": "timeframe",
        "title": "title",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        destinations: Union[DashboardReportDestination, UnsetType] = unset,
        modified_at: Union[datetime, none_type, UnsetType] = unset,
        schedule: Union[DashboardReportSchedule, UnsetType] = unset,
        template_variables: Union[DashboardReportTemplateVariables, UnsetType] = unset,
        timeframe: Union[DashboardReportTimeframe, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for the dashboard report schema.

        :param created_at: Date the report was created.
        :type created_at: datetime, optional

        :param description: Description of the report used in both the user interface, and as part of the email body for each report sent. Must be a UTF-8 encoded string less than 4 KiB in size.
        :type description: str, none_type, optional

        :param destinations: Report destination-specific configuration. This determines how reports are sent. Only email destinations are supported.
        :type destinations: DashboardReportDestination, optional

        :param modified_at: Date the report was most recently modified.
        :type modified_at: datetime, none_type, optional

        :param schedule: Report schedule-specific configuration that defines when and how often a report is sent.
        :type schedule: DashboardReportSchedule, optional

        :param template_variables: Template variables used to parameterize the dashboard when generating a report.
        :type template_variables: DashboardReportTemplateVariables, optional

        :param timeframe: Time period covered by the widgets in the dashboard report, at the time of report generation.
        :type timeframe: DashboardReportTimeframe, optional

        :param title: Title of the report in both the user interface, and as part of the email subject for each report sent.
        :type title: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if description is not unset:
            kwargs["description"] = description
        if destinations is not unset:
            kwargs["destinations"] = destinations
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if schedule is not unset:
            kwargs["schedule"] = schedule
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        if timeframe is not unset:
            kwargs["timeframe"] = timeframe
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
