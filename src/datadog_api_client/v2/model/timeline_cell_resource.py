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
    from datadog_api_client.v2.model.timeline_cell import TimelineCell
    from datadog_api_client.v2.model.timeline_cell_resource_type import TimelineCellResourceType


class TimelineCellResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeline_cell import TimelineCell
        from datadog_api_client.v2.model.timeline_cell_resource_type import TimelineCellResourceType

        return {
            "attributes": (TimelineCell,),
            "id": (str,),
            "type": (TimelineCellResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: TimelineCell, id: str, type: TimelineCellResourceType, **kwargs):
        """
        Timeline cell JSON:API resource

        :param attributes: timeline cell
        :type attributes: TimelineCell

        :param id: Timeline cell's identifier
        :type id: str

        :param type: Timeline cell JSON:API resource type
        :type type: TimelineCellResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
