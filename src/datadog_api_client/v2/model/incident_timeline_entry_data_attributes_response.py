# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_timeline_cell_type import IncidentTimelineCellType
    from datadog_api_client.v2.model.incident_timeline_entry_content import IncidentTimelineEntryContent
    from datadog_api_client.v2.model.incident_timeline_cell_source import IncidentTimelineCellSource


class IncidentTimelineEntryDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timeline_cell_type import IncidentTimelineCellType
        from datadog_api_client.v2.model.incident_timeline_entry_content import IncidentTimelineEntryContent
        from datadog_api_client.v2.model.incident_timeline_cell_source import IncidentTimelineCellSource

        return {
            "cell_type": (IncidentTimelineCellType,),
            "content": (IncidentTimelineEntryContent,),
            "created": (datetime,),
            "display_time": (datetime,),
            "important": (bool,),
            "incident_id": (str,),
            "modified": (datetime,),
            "parent_uuid": (str, none_type),
            "source": (IncidentTimelineCellSource,),
        }

    attribute_map = {
        "cell_type": "cell_type",
        "content": "content",
        "created": "created",
        "display_time": "display_time",
        "important": "important",
        "incident_id": "incident_id",
        "modified": "modified",
        "parent_uuid": "parent_uuid",
        "source": "source",
    }

    def __init__(
        self_,
        cell_type: IncidentTimelineCellType,
        content: IncidentTimelineEntryContent,
        created: datetime,
        display_time: datetime,
        important: bool,
        incident_id: str,
        modified: datetime,
        source: IncidentTimelineCellSource,
        parent_uuid: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a timeline entry.

        :param cell_type: The type of a timeline cell.
        :type cell_type: IncidentTimelineCellType

        :param content: The content of a timeline entry.
        :type content: IncidentTimelineEntryContent

        :param created: Timestamp when the entry was created.
        :type created: datetime

        :param display_time: The display time for this timeline entry.
        :type display_time: datetime

        :param important: Whether this timeline entry is marked as important.
        :type important: bool

        :param incident_id: The incident identifier.
        :type incident_id: str

        :param modified: Timestamp when the entry was last modified.
        :type modified: datetime

        :param parent_uuid: UUID of the parent timeline entry.
        :type parent_uuid: str, none_type, optional

        :param source: The source of a timeline cell.
        :type source: IncidentTimelineCellSource
        """
        if parent_uuid is not unset:
            kwargs["parent_uuid"] = parent_uuid
        super().__init__(kwargs)

        self_.cell_type = cell_type
        self_.content = content
        self_.created = created
        self_.display_time = display_time
        self_.important = important
        self_.incident_id = incident_id
        self_.modified = modified
        self_.source = source
