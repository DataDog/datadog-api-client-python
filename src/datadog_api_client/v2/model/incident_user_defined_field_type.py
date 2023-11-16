# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentUserDefinedFieldType(ModelSimple):
    """
    The incident user defined fields type.

    :param value: If omitted defaults to "user_defined_field". Must be one of ["user_defined_field"].
    :type value: str
    """

    allowed_values = {
        "user_defined_field",
    }
    USER_DEFINED_FIELD: ClassVar["IncidentUserDefinedFieldType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentUserDefinedFieldType.USER_DEFINED_FIELD = IncidentUserDefinedFieldType("user_defined_field")
