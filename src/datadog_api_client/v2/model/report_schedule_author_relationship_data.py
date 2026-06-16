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
    from datadog_api_client.v2.model.report_schedule_author_type import ReportScheduleAuthorType


class ReportScheduleAuthorRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_author_type import ReportScheduleAuthorType

        return {
            "id": (str,),
            "type": (ReportScheduleAuthorType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ReportScheduleAuthorType, **kwargs):
        """
        Relationship data for the author of the report schedule.

        :param id: The user UUID of the report schedule author.
        :type id: str

        :param type: JSON:API resource type for the included report author.
        :type type: ReportScheduleAuthorType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
