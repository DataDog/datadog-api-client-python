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
    from datadog_api_client.v2.model.report_schedule_create_request_attributes import (
        ReportScheduleCreateRequestAttributes,
    )
    from datadog_api_client.v2.model.report_schedule_type import ReportScheduleType


class ReportScheduleCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_create_request_attributes import (
            ReportScheduleCreateRequestAttributes,
        )
        from datadog_api_client.v2.model.report_schedule_type import ReportScheduleType

        return {
            "attributes": (ReportScheduleCreateRequestAttributes,),
            "type": (ReportScheduleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: ReportScheduleCreateRequestAttributes, type: ReportScheduleType, **kwargs):
        """
        The JSON:API data object for a report schedule creation request.

        :param attributes: The configuration of the report schedule to create.
        :type attributes: ReportScheduleCreateRequestAttributes

        :param type: JSON:API resource type for report schedules.
        :type type: ReportScheduleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
