# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dataset_report_schedule_resource_type import DatasetReportScheduleResourceType
    from datadog_api_client.v2.model.report_schedule_status import ReportScheduleStatus


class DatasetReportScheduleResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_report_schedule_resource_type import DatasetReportScheduleResourceType
        from datadog_api_client.v2.model.report_schedule_status import ReportScheduleStatus

        return {
            "cell_id": (str, none_type),
            "dataset_id": (str, none_type),
            "description": (str,),
            "file_row_limit": (int, none_type),
            "inline_row_limit": (int, none_type),
            "next_recurrence": (int, none_type),
            "notebook_id": (int, none_type),
            "recipients": ([str],),
            "resource_id": (str,),
            "resource_type": (DatasetReportScheduleResourceType,),
            "rrule": (str,),
            "status": (ReportScheduleStatus,),
            "timeframe": (str,),
            "timezone": (str,),
            "title": (str,),
        }

    attribute_map = {
        "cell_id": "cell_id",
        "dataset_id": "dataset_id",
        "description": "description",
        "file_row_limit": "file_row_limit",
        "inline_row_limit": "inline_row_limit",
        "next_recurrence": "next_recurrence",
        "notebook_id": "notebook_id",
        "recipients": "recipients",
        "resource_id": "resource_id",
        "resource_type": "resource_type",
        "rrule": "rrule",
        "status": "status",
        "timeframe": "timeframe",
        "timezone": "timezone",
        "title": "title",
    }

    def __init__(
        self_,
        cell_id: Union[str, none_type],
        dataset_id: Union[str, none_type],
        description: str,
        file_row_limit: Union[int, none_type],
        inline_row_limit: Union[int, none_type],
        next_recurrence: Union[int, none_type],
        notebook_id: Union[int, none_type],
        recipients: List[str],
        resource_id: str,
        resource_type: DatasetReportScheduleResourceType,
        rrule: str,
        status: ReportScheduleStatus,
        timeframe: str,
        timezone: str,
        title: str,
        **kwargs,
    ):
        """
        The configuration and derived state of a report schedule for a published dataset.

        :param cell_id: The identifier of the notebook cell that published the dataset, or ``null`` if not set.
        :type cell_id: str, none_type

        :param dataset_id: The identifier of the dataset, or ``null`` if not set.
        :type dataset_id: str, none_type

        :param description: The description of the report.
        :type description: str

        :param file_row_limit: The maximum number of rows included in the attached CSV file, or ``null`` if not set.
        :type file_row_limit: int, none_type

        :param inline_row_limit: The maximum number of rows included inline in the email body, or ``null`` if not set.
        :type inline_row_limit: int, none_type

        :param next_recurrence: The Unix timestamp, in milliseconds, of the next scheduled delivery, or
            ``null`` if none is scheduled.
        :type next_recurrence: int, none_type

        :param notebook_id: The identifier of the notebook containing the dataset cell, or ``null`` if not set.
        :type notebook_id: int, none_type

        :param recipients: The recipients of the report (email addresses, Slack channel references, or
            Microsoft Teams channel references).
        :type recipients: [str]

        :param resource_id: The identifier of the widget containing the dataset.
        :type resource_id: str

        :param resource_type: The type of resource targeted by a dataset report schedule.
        :type resource_type: DatasetReportScheduleResourceType

        :param rrule: The recurrence rule for the schedule, expressed as an iCalendar ``RRULE`` string.
        :type rrule: str

        :param status: Whether the schedule is currently delivering reports ( ``active`` ) or paused ( ``inactive`` ).
        :type status: ReportScheduleStatus

        :param timeframe: The relative timeframe of data included in the report.
        :type timeframe: str

        :param timezone: The IANA time zone identifier the recurrence rule is evaluated in.
        :type timezone: str

        :param title: The title of the report.
        :type title: str
        """
        super().__init__(kwargs)

        self_.cell_id = cell_id
        self_.dataset_id = dataset_id
        self_.description = description
        self_.file_row_limit = file_row_limit
        self_.inline_row_limit = inline_row_limit
        self_.next_recurrence = next_recurrence
        self_.notebook_id = notebook_id
        self_.recipients = recipients
        self_.resource_id = resource_id
        self_.resource_type = resource_type
        self_.rrule = rrule
        self_.status = status
        self_.timeframe = timeframe
        self_.timezone = timezone
        self_.title = title
