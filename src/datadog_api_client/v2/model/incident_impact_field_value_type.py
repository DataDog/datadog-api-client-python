# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentImpactFieldValueType(ModelSimple):
    """
    The type of an impact field.

    :param value: Must be one of ["dropdown", "text", "textarray", "metrictag", "number", "datetime", "multiselect"].
    :type value: str
    """

    allowed_values = {
        "dropdown",
        "text",
        "textarray",
        "metrictag",
        "number",
        "datetime",
        "multiselect",
    }
    DROPDOWN: ClassVar["IncidentImpactFieldValueType"]
    TEXT: ClassVar["IncidentImpactFieldValueType"]
    TEXTARRAY: ClassVar["IncidentImpactFieldValueType"]
    METRICTAG: ClassVar["IncidentImpactFieldValueType"]
    NUMBER: ClassVar["IncidentImpactFieldValueType"]
    DATETIME: ClassVar["IncidentImpactFieldValueType"]
    MULTISELECT: ClassVar["IncidentImpactFieldValueType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentImpactFieldValueType.DROPDOWN = IncidentImpactFieldValueType("dropdown")
IncidentImpactFieldValueType.TEXT = IncidentImpactFieldValueType("text")
IncidentImpactFieldValueType.TEXTARRAY = IncidentImpactFieldValueType("textarray")
IncidentImpactFieldValueType.METRICTAG = IncidentImpactFieldValueType("metrictag")
IncidentImpactFieldValueType.NUMBER = IncidentImpactFieldValueType("number")
IncidentImpactFieldValueType.DATETIME = IncidentImpactFieldValueType("datetime")
IncidentImpactFieldValueType.MULTISELECT = IncidentImpactFieldValueType("multiselect")
