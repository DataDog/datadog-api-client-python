# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class EventTimelineWidgetDefinitionType(StringEnum):
    """
    Type of the event timeline widget.

    :param value: If omitted defaults to "event_timeline". Must be one of ["event_timeline"].
    :type value: str
    """

    allowed_values = {
        "event_timeline",
    }
    EVENT_TIMELINE: ClassVar["EventTimelineWidgetDefinitionType"]


EventTimelineWidgetDefinitionType.EVENT_TIMELINE = EventTimelineWidgetDefinitionType("event_timeline")
