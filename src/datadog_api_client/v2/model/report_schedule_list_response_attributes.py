# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.report_schedule_response_attributes_delivery_format import (
        ReportScheduleResponseAttributesDeliveryFormat,
    )
    from datadog_api_client.v2.model.report_schedule_query_parameter_value import ReportScheduleQueryParameterValue
    from datadog_api_client.v2.model.report_schedule_resource_type import ReportScheduleResourceType
    from datadog_api_client.v2.model.report_schedule_status import ReportScheduleStatus
    from datadog_api_client.v2.model.report_schedule_template_variable import ReportScheduleTemplateVariable


class ReportScheduleListResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_response_attributes_delivery_format import (
            ReportScheduleResponseAttributesDeliveryFormat,
        )
        from datadog_api_client.v2.model.report_schedule_query_parameter_value import ReportScheduleQueryParameterValue
        from datadog_api_client.v2.model.report_schedule_resource_type import ReportScheduleResourceType
        from datadog_api_client.v2.model.report_schedule_status import ReportScheduleStatus
        from datadog_api_client.v2.model.report_schedule_template_variable import ReportScheduleTemplateVariable

        return {
            "delivery_format": (ReportScheduleResponseAttributesDeliveryFormat,),
            "description": (str,),
            "next_recurrence": (int, none_type),
            "query_params": ({str: (ReportScheduleQueryParameterValue,)},),
            "recipients": ([str],),
            "resource_id": (str,),
            "resource_type": (ReportScheduleResourceType,),
            "rrule": (str,),
            "status": (ReportScheduleStatus,),
            "template_variables": ([ReportScheduleTemplateVariable],),
            "timeframe": (str, none_type),
            "timezone": (str,),
            "title": (str,),
        }

    attribute_map = {
        "delivery_format": "delivery_format",
        "description": "description",
        "next_recurrence": "next_recurrence",
        "query_params": "query_params",
        "recipients": "recipients",
        "resource_id": "resource_id",
        "resource_type": "resource_type",
        "rrule": "rrule",
        "status": "status",
        "template_variables": "template_variables",
        "timeframe": "timeframe",
        "timezone": "timezone",
        "title": "title",
    }

    def __init__(
        self_,
        description: str,
        next_recurrence: Union[int, none_type],
        query_params: Dict[str, Union[ReportScheduleQueryParameterValue, str, List[str]]],
        recipients: List[str],
        resource_id: str,
        resource_type: ReportScheduleResourceType,
        rrule: str,
        status: ReportScheduleStatus,
        template_variables: List[ReportScheduleTemplateVariable],
        timeframe: Union[str, none_type],
        timezone: str,
        title: str,
        delivery_format: Union[ReportScheduleResponseAttributesDeliveryFormat, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The configuration and derived state of a report schedule in a list response.

        :param delivery_format: The delivery format for dashboard report schedules, or ``null`` if not set.
        :type delivery_format: ReportScheduleResponseAttributesDeliveryFormat, none_type, optional

        :param description: The description of the report.
        :type description: str

        :param next_recurrence: The Unix timestamp, in milliseconds, of the next scheduled delivery, or ``null`` if none is scheduled.
        :type next_recurrence: int, none_type

        :param query_params: Query parameters applied when rendering the report.
        :type query_params: {str: (ReportScheduleQueryParameterValue,)}

        :param recipients: The recipients of the report (email addresses, Slack channel references, or Microsoft Teams channel references).
        :type recipients: [str]

        :param resource_id: The identifier of the resource rendered in the report.
        :type resource_id: str

        :param resource_type: The type of dashboard resource the report schedule targets.
        :type resource_type: ReportScheduleResourceType

        :param rrule: The recurrence rule for the schedule, expressed as an iCalendar ``RRULE`` string.
        :type rrule: str

        :param status: Whether the schedule is currently delivering reports ( ``active`` ) or paused ( ``inactive`` ).
        :type status: ReportScheduleStatus

        :param template_variables: The dashboard template variables applied when rendering the report.
        :type template_variables: [ReportScheduleTemplateVariable]

        :param timeframe: The relative timeframe of data included in the report, or ``null`` if not set.
        :type timeframe: str, none_type

        :param timezone: The IANA time zone identifier the recurrence rule is evaluated in.
        :type timezone: str

        :param title: The title of the report.
        :type title: str
        """
        if delivery_format is not unset:
            kwargs["delivery_format"] = delivery_format
        super().__init__(kwargs)

        self_.description = description
        self_.next_recurrence = next_recurrence
        self_.query_params = query_params
        self_.recipients = recipients
        self_.resource_id = resource_id
        self_.resource_type = resource_type
        self_.rrule = rrule
        self_.status = status
        self_.template_variables = template_variables
        self_.timeframe = timeframe
        self_.timezone = timezone
        self_.title = title
