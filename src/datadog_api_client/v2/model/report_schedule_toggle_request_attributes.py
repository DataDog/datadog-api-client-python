# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.report_schedule_status import ReportScheduleStatus


class ReportScheduleToggleRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_status import ReportScheduleStatus

        return {
            "status": (ReportScheduleStatus,),
        }

    attribute_map = {
        "status": "status",
    }

    def __init__(self_, status: ReportScheduleStatus, **kwargs):
        """
        The status to set on the report schedule.

        :param status: Whether the schedule is currently delivering reports ( ``active`` ) or paused ( ``inactive`` ).
        :type status: ReportScheduleStatus
        """
        super().__init__(kwargs)

        self_.status = status
