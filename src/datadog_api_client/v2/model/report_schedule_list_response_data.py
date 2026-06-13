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
    from datadog_api_client.v2.model.report_schedule_list_response_attributes import (
        ReportScheduleListResponseAttributes,
    )
    from datadog_api_client.v2.model.report_schedule_list_response_relationships import (
        ReportScheduleListResponseRelationships,
    )
    from datadog_api_client.v2.model.report_schedule_type import ReportScheduleType


class ReportScheduleListResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_list_response_attributes import (
            ReportScheduleListResponseAttributes,
        )
        from datadog_api_client.v2.model.report_schedule_list_response_relationships import (
            ReportScheduleListResponseRelationships,
        )
        from datadog_api_client.v2.model.report_schedule_type import ReportScheduleType

        return {
            "attributes": (ReportScheduleListResponseAttributes,),
            "id": (str,),
            "relationships": (ReportScheduleListResponseRelationships,),
            "type": (ReportScheduleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ReportScheduleListResponseAttributes,
        id: str,
        relationships: ReportScheduleListResponseRelationships,
        type: ReportScheduleType,
        **kwargs,
    ):
        """
        The JSON:API data object representing a report schedule in a list response.

        :param attributes: The configuration and derived state of a report schedule in a list response.
        :type attributes: ReportScheduleListResponseAttributes

        :param id: The unique identifier of the report schedule.
        :type id: str

        :param relationships: Relationships for a report schedule in a list response.
        :type relationships: ReportScheduleListResponseRelationships

        :param type: JSON:API resource type for report schedules.
        :type type: ReportScheduleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
