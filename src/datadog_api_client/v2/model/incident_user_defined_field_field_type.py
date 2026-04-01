# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentUserDefinedFieldFieldType(ModelSimple):
    """
    The data type of the field. 1=dropdown, 2=multiselect, 3=textbox, 4=textarray, 5=metrictag, 6=autocomplete, 7=number, 8=datetime.

    :param value: Must be one of [1, 2, 3, 4, 5, 6, 7, 8].
    :type value: int
    """

    allowed_values = {
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
    }
    DROPDOWN: ClassVar["IncidentUserDefinedFieldFieldType"]
    MULTISELECT: ClassVar["IncidentUserDefinedFieldFieldType"]
    TEXTBOX: ClassVar["IncidentUserDefinedFieldFieldType"]
    TEXTARRAY: ClassVar["IncidentUserDefinedFieldFieldType"]
    METRICTAG: ClassVar["IncidentUserDefinedFieldFieldType"]
    AUTOCOMPLETE: ClassVar["IncidentUserDefinedFieldFieldType"]
    NUMBER: ClassVar["IncidentUserDefinedFieldFieldType"]
    DATETIME: ClassVar["IncidentUserDefinedFieldFieldType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }


IncidentUserDefinedFieldFieldType.DROPDOWN = IncidentUserDefinedFieldFieldType(1)
IncidentUserDefinedFieldFieldType.MULTISELECT = IncidentUserDefinedFieldFieldType(2)
IncidentUserDefinedFieldFieldType.TEXTBOX = IncidentUserDefinedFieldFieldType(3)
IncidentUserDefinedFieldFieldType.TEXTARRAY = IncidentUserDefinedFieldFieldType(4)
IncidentUserDefinedFieldFieldType.METRICTAG = IncidentUserDefinedFieldFieldType(5)
IncidentUserDefinedFieldFieldType.AUTOCOMPLETE = IncidentUserDefinedFieldFieldType(6)
IncidentUserDefinedFieldFieldType.NUMBER = IncidentUserDefinedFieldFieldType(7)
IncidentUserDefinedFieldFieldType.DATETIME = IncidentUserDefinedFieldFieldType(8)
