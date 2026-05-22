# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentTimelineCellType(ModelSimple):
    """
    The type of a timeline cell.

    :param value: Must be one of ["markdown", "incident_status_change", "timestamp_change", "meeting_summary", "meeting_chat", "role_assignment_change", "postmortem_change"].
    :type value: str
    """

    allowed_values = {
        "markdown",
        "incident_status_change",
        "timestamp_change",
        "meeting_summary",
        "meeting_chat",
        "role_assignment_change",
        "postmortem_change",
    }
    MARKDOWN: ClassVar["IncidentTimelineCellType"]
    INCIDENT_STATUS_CHANGE: ClassVar["IncidentTimelineCellType"]
    TIMESTAMP_CHANGE: ClassVar["IncidentTimelineCellType"]
    MEETING_SUMMARY: ClassVar["IncidentTimelineCellType"]
    MEETING_CHAT: ClassVar["IncidentTimelineCellType"]
    ROLE_ASSIGNMENT_CHANGE: ClassVar["IncidentTimelineCellType"]
    POSTMORTEM_CHANGE: ClassVar["IncidentTimelineCellType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentTimelineCellType.MARKDOWN = IncidentTimelineCellType("markdown")
IncidentTimelineCellType.INCIDENT_STATUS_CHANGE = IncidentTimelineCellType("incident_status_change")
IncidentTimelineCellType.TIMESTAMP_CHANGE = IncidentTimelineCellType("timestamp_change")
IncidentTimelineCellType.MEETING_SUMMARY = IncidentTimelineCellType("meeting_summary")
IncidentTimelineCellType.MEETING_CHAT = IncidentTimelineCellType("meeting_chat")
IncidentTimelineCellType.ROLE_ASSIGNMENT_CHANGE = IncidentTimelineCellType("role_assignment_change")
IncidentTimelineCellType.POSTMORTEM_CHANGE = IncidentTimelineCellType("postmortem_change")
