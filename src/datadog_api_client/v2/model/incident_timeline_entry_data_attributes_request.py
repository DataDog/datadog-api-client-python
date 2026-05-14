# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_timeline_cell_type import IncidentTimelineCellType
    from datadog_api_client.v2.model.incident_timeline_entry_content import IncidentTimelineEntryContent


class IncidentTimelineEntryDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timeline_cell_type import IncidentTimelineCellType
        from datadog_api_client.v2.model.incident_timeline_entry_content import IncidentTimelineEntryContent

        return {
            "cell_type": (IncidentTimelineCellType,),
            "content": (IncidentTimelineEntryContent,),
            "display_time": (datetime,),
            "important": (bool,),
        }

    attribute_map = {
        "cell_type": "cell_type",
        "content": "content",
        "display_time": "display_time",
        "important": "important",
    }

    def __init__(
        self_,
        cell_type: IncidentTimelineCellType,
        content: IncidentTimelineEntryContent,
        display_time: Union[datetime, UnsetType] = unset,
        important: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a timeline entry.

        :param cell_type: The type of a timeline cell.
        :type cell_type: IncidentTimelineCellType

        :param content: The content of a timeline entry.
        :type content: IncidentTimelineEntryContent

        :param display_time: The display time for this timeline entry.
        :type display_time: datetime, optional

        :param important: Whether this timeline entry is marked as important.
        :type important: bool, optional
        """
        if display_time is not unset:
            kwargs["display_time"] = display_time
        if important is not unset:
            kwargs["important"] = important
        super().__init__(kwargs)

        self_.cell_type = cell_type
        self_.content = content
