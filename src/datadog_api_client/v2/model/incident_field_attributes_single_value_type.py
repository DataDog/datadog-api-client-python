# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class IncidentFieldAttributesSingleValueType(StringEnum):
    """
    Type of the single value field definitions.

    :param value: If omitted defaults to "dropdown". Must be one of ["dropdown", "textbox"].
    :type value: str
    """

    allowed_values = {
        "dropdown",
        "textbox",
    }
    DROPDOWN: ClassVar["IncidentFieldAttributesSingleValueType"]
    TEXTBOX: ClassVar["IncidentFieldAttributesSingleValueType"]


IncidentFieldAttributesSingleValueType.DROPDOWN = IncidentFieldAttributesSingleValueType("dropdown")
IncidentFieldAttributesSingleValueType.TEXTBOX = IncidentFieldAttributesSingleValueType("textbox")
