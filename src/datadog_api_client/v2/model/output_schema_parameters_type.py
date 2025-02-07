# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OutputSchemaParametersType(ModelSimple):
    """
    The definition of `OutputSchemaParametersType` object.

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
    STRING: ClassVar["OutputSchemaParametersType"]
    NUMBER: ClassVar["OutputSchemaParametersType"]
    BOOLEAN: ClassVar["OutputSchemaParametersType"]
    OBJECT: ClassVar["OutputSchemaParametersType"]
    ARRAY_STRING: ClassVar["OutputSchemaParametersType"]
    ARRAY_NUMBER: ClassVar["OutputSchemaParametersType"]
    ARRAY_BOOLEAN: ClassVar["OutputSchemaParametersType"]
    ARRAY_OBJECT: ClassVar["OutputSchemaParametersType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OutputSchemaParametersType.STRING = OutputSchemaParametersType("STRING")
OutputSchemaParametersType.NUMBER = OutputSchemaParametersType("NUMBER")
OutputSchemaParametersType.BOOLEAN = OutputSchemaParametersType("BOOLEAN")
OutputSchemaParametersType.OBJECT = OutputSchemaParametersType("OBJECT")
OutputSchemaParametersType.ARRAY_STRING = OutputSchemaParametersType("ARRAY_STRING")
OutputSchemaParametersType.ARRAY_NUMBER = OutputSchemaParametersType("ARRAY_NUMBER")
OutputSchemaParametersType.ARRAY_BOOLEAN = OutputSchemaParametersType("ARRAY_BOOLEAN")
OutputSchemaParametersType.ARRAY_OBJECT = OutputSchemaParametersType("ARRAY_OBJECT")
