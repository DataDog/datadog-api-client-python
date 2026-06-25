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
    from datadog_api_client.v2.model.report_schedule_included_resource_type import ReportScheduleIncludedResourceType


class ReportScheduleListResourceRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_included_resource_type import (
            ReportScheduleIncludedResourceType,
        )

        return {
            "id": (str,),
            "type": (ReportScheduleIncludedResourceType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ReportScheduleIncludedResourceType, **kwargs):
        """
        Relationship data for the report target resource.

        :param id: The resource identifier.
        :type id: str

        :param type: JSON:API resource type for an included report resource.
        :type type: ReportScheduleIncludedResourceType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
