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
    from datadog_api_client.v2.model.report_schedule_author_relationship_data import (
        ReportScheduleAuthorRelationshipData,
    )


class ReportScheduleAuthorRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_author_relationship_data import (
            ReportScheduleAuthorRelationshipData,
        )

        return {
            "data": (ReportScheduleAuthorRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ReportScheduleAuthorRelationshipData, **kwargs):
        """
        Relationship to the author of the report schedule.

        :param data: Relationship data for the author of the report schedule.
        :type data: ReportScheduleAuthorRelationshipData
        """
        super().__init__(kwargs)

        self_.data = data
