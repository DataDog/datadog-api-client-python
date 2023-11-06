# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class NoteWidgetDefinitionType(StringEnum):
    """
    Type of the note widget.

    :param value: If omitted defaults to "note". Must be one of ["note"].
    :type value: str
    """

    allowed_values = {
        "note",
    }
    NOTE: ClassVar["NoteWidgetDefinitionType"]


NoteWidgetDefinitionType.NOTE = NoteWidgetDefinitionType("note")
