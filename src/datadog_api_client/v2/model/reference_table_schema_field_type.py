# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ReferenceTableSchemaFieldType(ModelSimple):
    """
    The field type for reference table schema fields.

    :param value: Must be one of ["STRING", "INT32"].
    :type value: str
    """

    allowed_values = {
        "STRING",
        "INT32",
    }
    STRING: ClassVar["ReferenceTableSchemaFieldType"]
    INT32: ClassVar["ReferenceTableSchemaFieldType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ReferenceTableSchemaFieldType.STRING = ReferenceTableSchemaFieldType("STRING")
ReferenceTableSchemaFieldType.INT32 = ReferenceTableSchemaFieldType("INT32")
