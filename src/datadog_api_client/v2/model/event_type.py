# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class EventType(StringEnum):
    """
    Type of the event.

    :param value: If omitted defaults to "event". Must be one of ["event"].
    :type value: str
    """

    allowed_values = {
        "event",
    }
    EVENT: ClassVar["EventType"]


EventType.EVENT = EventType("event")
