# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dataset_report_schedule_response_attributes import (
        DatasetReportScheduleResponseAttributes,
    )
    from datadog_api_client.v2.model.report_schedule_response_relationships import ReportScheduleResponseRelationships
    from datadog_api_client.v2.model.report_schedule_type import ReportScheduleType


class DatasetReportScheduleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_report_schedule_response_attributes import (
            DatasetReportScheduleResponseAttributes,
        )
        from datadog_api_client.v2.model.report_schedule_response_relationships import (
            ReportScheduleResponseRelationships,
        )
        from datadog_api_client.v2.model.report_schedule_type import ReportScheduleType

        return {
            "attributes": (DatasetReportScheduleResponseAttributes,),
            "id": (UUID,),
            "relationships": (ReportScheduleResponseRelationships,),
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
        attributes: DatasetReportScheduleResponseAttributes,
        id: UUID,
        relationships: ReportScheduleResponseRelationships,
        type: ReportScheduleType,
        **kwargs,
    ):
        """
        The JSON:API data object representing a dataset report schedule.

        :param attributes: The configuration and derived state of a report schedule for a published dataset.
        :type attributes: DatasetReportScheduleResponseAttributes

        :param id: The unique identifier of the dataset report schedule.
        :type id: UUID

        :param relationships: Relationships for the report schedule.
        :type relationships: ReportScheduleResponseRelationships

        :param type: JSON:API resource type for report schedules.
        :type type: ReportScheduleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
