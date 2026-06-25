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
    from datadog_api_client.v2.model.report_schedule_toggle_request_attributes import (
        ReportScheduleToggleRequestAttributes,
    )
    from datadog_api_client.v2.model.report_schedule_type import ReportScheduleType


class ReportScheduleToggleRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_toggle_request_attributes import (
            ReportScheduleToggleRequestAttributes,
        )
        from datadog_api_client.v2.model.report_schedule_type import ReportScheduleType

        return {
            "attributes": (ReportScheduleToggleRequestAttributes,),
            "type": (ReportScheduleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: ReportScheduleToggleRequestAttributes, type: ReportScheduleType, **kwargs):
        """
        The JSON:API data object for a report schedule toggle request.

        :param attributes: The status to set on the report schedule.
        :type attributes: ReportScheduleToggleRequestAttributes

        :param type: JSON:API resource type for report schedules.
        :type type: ReportScheduleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
