# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.report_schedule_delivery_format import ReportScheduleDeliveryFormat
    from datadog_api_client.v2.model.report_schedule_template_variable import ReportScheduleTemplateVariable


class ReportSchedulePatchRequestAttributes(ModelNormal):
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
        from datadog_api_client.v2.model.report_schedule_delivery_format import ReportScheduleDeliveryFormat
        from datadog_api_client.v2.model.report_schedule_template_variable import ReportScheduleTemplateVariable

        return {
            "delivery_format": (ReportScheduleDeliveryFormat,),
            "description": (str,),
            "recipients": ([str],),
            "rrule": (str,),
            "tab_id": (UUID,),
            "template_variables": ([ReportScheduleTemplateVariable],),
            "timeframe": (str,),
            "timezone": (str,),
            "title": (str,),
        }

    attribute_map = {
        "delivery_format": "delivery_format",
        "description": "description",
        "recipients": "recipients",
        "rrule": "rrule",
        "tab_id": "tab_id",
        "template_variables": "template_variables",
        "timeframe": "timeframe",
        "timezone": "timezone",
        "title": "title",
    }

    def __init__(
        self_,
        description: str,
        recipients: List[str],
        rrule: str,
        template_variables: List[ReportScheduleTemplateVariable],
        timeframe: str,
        timezone: str,
        title: str,
        delivery_format: Union[ReportScheduleDeliveryFormat, UnsetType] = unset,
        tab_id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        The updated configuration of the report schedule. These values replace the existing
        ones; the targeted resource ( ``resource_id`` and ``resource_type`` ) cannot be changed.

        :param delivery_format: How a PDF-export report is delivered. ``pdf`` attaches a PDF file, ``png`` embeds
            an inline PNG image, and ``pdf_and_png`` delivers both.
        :type delivery_format: ReportScheduleDeliveryFormat, optional

        :param description: A description of the report, up to 4096 characters.
        :type description: str

        :param recipients: The recipients of the report. Each entry is an email address, a Slack channel
            reference in the form ``slack:{team_id}.{channel_id}.{channel_name}`` , or a Microsoft
            Teams channel reference in the form ``teams:{tenant_id}|{team_id}|{channel_id}``.
        :type recipients: [str]

        :param rrule: The recurrence rule for the schedule, expressed as an iCalendar ``RRULE`` string.
        :type rrule: str

        :param tab_id: The identifier of the dashboard tab to render, when the dashboard has tabs.
        :type tab_id: UUID, optional

        :param template_variables: The dashboard template variables applied when rendering the report.
        :type template_variables: [ReportScheduleTemplateVariable]

        :param timeframe: The relative timeframe of data to include in the report.
        :type timeframe: str

        :param timezone: The IANA time zone identifier the recurrence rule is evaluated in.
        :type timezone: str

        :param title: The title of the report, between 1 and 78 characters.
        :type title: str
        """
        if delivery_format is not unset:
            kwargs["delivery_format"] = delivery_format
        if tab_id is not unset:
            kwargs["tab_id"] = tab_id
        super().__init__(kwargs)

        self_.description = description
        self_.recipients = recipients
        self_.rrule = rrule
        self_.template_variables = template_variables
        self_.timeframe = timeframe
        self_.timezone = timezone
        self_.title = title
