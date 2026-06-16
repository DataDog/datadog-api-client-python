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
    from datadog_api_client.v2.model.report_schedule_author_relationship import ReportScheduleAuthorRelationship


class ReportScheduleResponseRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_author_relationship import ReportScheduleAuthorRelationship

        return {
            "author": (ReportScheduleAuthorRelationship,),
        }

    attribute_map = {
        "author": "author",
    }

    def __init__(self_, author: ReportScheduleAuthorRelationship, **kwargs):
        """
        Relationships for the report schedule.

        :param author: Relationship to the author of the report schedule.
        :type author: ReportScheduleAuthorRelationship
        """
        super().__init__(kwargs)

        self_.author = author
