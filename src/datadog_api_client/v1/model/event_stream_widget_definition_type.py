# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class EventStreamWidgetDefinitionType(StringEnum):
    """
    Type of the event stream widget.

    :param value: If omitted defaults to "event_stream". Must be one of ["event_stream"].
    :type value: str
    """

    allowed_values = {
        "event_stream",
    }
    EVENT_STREAM: ClassVar["EventStreamWidgetDefinitionType"]


EventStreamWidgetDefinitionType.EVENT_STREAM = EventStreamWidgetDefinitionType("event_stream")
