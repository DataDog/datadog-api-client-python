# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class InputSchemaParametersType(ModelSimple):
    """
    The definition of `InputSchemaParametersType` object.

    :param value: Must be one of ["STRING", "NUMBER", "BOOLEAN", "OBJECT", "ARRAY_STRING", "ARRAY_NUMBER", "ARRAY_BOOLEAN", "ARRAY_OBJECT"].
    :type value: str
    """

    allowed_values = {
        "STRING",
        "NUMBER",
        "BOOLEAN",
        "OBJECT",
        "ARRAY_STRING",
        "ARRAY_NUMBER",
        "ARRAY_BOOLEAN",
        "ARRAY_OBJECT",
    }
    STRING: ClassVar["InputSchemaParametersType"]
    NUMBER: ClassVar["InputSchemaParametersType"]
    BOOLEAN: ClassVar["InputSchemaParametersType"]
    OBJECT: ClassVar["InputSchemaParametersType"]
    ARRAY_STRING: ClassVar["InputSchemaParametersType"]
    ARRAY_NUMBER: ClassVar["InputSchemaParametersType"]
    ARRAY_BOOLEAN: ClassVar["InputSchemaParametersType"]
    ARRAY_OBJECT: ClassVar["InputSchemaParametersType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


InputSchemaParametersType.STRING = InputSchemaParametersType("STRING")
InputSchemaParametersType.NUMBER = InputSchemaParametersType("NUMBER")
InputSchemaParametersType.BOOLEAN = InputSchemaParametersType("BOOLEAN")
InputSchemaParametersType.OBJECT = InputSchemaParametersType("OBJECT")
InputSchemaParametersType.ARRAY_STRING = InputSchemaParametersType("ARRAY_STRING")
InputSchemaParametersType.ARRAY_NUMBER = InputSchemaParametersType("ARRAY_NUMBER")
InputSchemaParametersType.ARRAY_BOOLEAN = InputSchemaParametersType("ARRAY_BOOLEAN")
InputSchemaParametersType.ARRAY_OBJECT = InputSchemaParametersType("ARRAY_OBJECT")
