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
    from datadog_api_client.v2.model.report_schedule_author_attributes import ReportScheduleAuthorAttributes
    from datadog_api_client.v2.model.report_schedule_author_type import ReportScheduleAuthorType


class ReportScheduleAuthor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_author_attributes import ReportScheduleAuthorAttributes
        from datadog_api_client.v2.model.report_schedule_author_type import ReportScheduleAuthorType

        return {
            "attributes": (ReportScheduleAuthorAttributes,),
            "id": (str,),
            "type": (ReportScheduleAuthorType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ReportScheduleAuthorAttributes, id: str, type: ReportScheduleAuthorType, **kwargs):
        """
        A user included as a related JSON:API resource.

        :param attributes: Attributes of the report author.
        :type attributes: ReportScheduleAuthorAttributes

        :param id: The user UUID.
        :type id: str

        :param type: JSON:API resource type for the included report author.
        :type type: ReportScheduleAuthorType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
