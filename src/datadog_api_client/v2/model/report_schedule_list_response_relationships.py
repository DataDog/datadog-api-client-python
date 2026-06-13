# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.report_schedule_author_relationship import ReportScheduleAuthorRelationship
    from datadog_api_client.v2.model.report_schedule_list_resource_relationship import (
        ReportScheduleListResourceRelationship,
    )


class ReportScheduleListResponseRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_author_relationship import ReportScheduleAuthorRelationship
        from datadog_api_client.v2.model.report_schedule_list_resource_relationship import (
            ReportScheduleListResourceRelationship,
        )

        return {
            "author": (ReportScheduleAuthorRelationship,),
            "resource": (ReportScheduleListResourceRelationship,),
        }

    attribute_map = {
        "author": "author",
        "resource": "resource",
    }

    def __init__(
        self_,
        author: ReportScheduleAuthorRelationship,
        resource: Union[ReportScheduleListResourceRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships for a report schedule in a list response.

        :param author: Relationship to the author of the report schedule.
        :type author: ReportScheduleAuthorRelationship

        :param resource: Relationship to the report target resource.
        :type resource: ReportScheduleListResourceRelationship, optional
        """
        if resource is not unset:
            kwargs["resource"] = resource
        super().__init__(kwargs)

        self_.author = author
