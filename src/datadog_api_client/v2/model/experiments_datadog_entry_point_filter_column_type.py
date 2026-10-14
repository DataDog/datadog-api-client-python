# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsDatadogEntryPointFilterColumnType(ModelSimple):
    """
    Data type of the column evaluated by the entry-point filter.

    :param value: Must be one of ["varchar", "int", "double", "boolean", "varchar_array", "int_array", "double_array", "raw"].
    :type value: str
    """

    allowed_values = {
        "varchar",
        "int",
        "double",
        "boolean",
        "varchar_array",
        "int_array",
        "double_array",
        "raw",
    }
    VARCHAR: ClassVar["ExperimentsDatadogEntryPointFilterColumnType"]
    INT: ClassVar["ExperimentsDatadogEntryPointFilterColumnType"]
    DOUBLE: ClassVar["ExperimentsDatadogEntryPointFilterColumnType"]
    BOOLEAN: ClassVar["ExperimentsDatadogEntryPointFilterColumnType"]
    VARCHAR_ARRAY: ClassVar["ExperimentsDatadogEntryPointFilterColumnType"]
    INT_ARRAY: ClassVar["ExperimentsDatadogEntryPointFilterColumnType"]
    DOUBLE_ARRAY: ClassVar["ExperimentsDatadogEntryPointFilterColumnType"]
    RAW: ClassVar["ExperimentsDatadogEntryPointFilterColumnType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsDatadogEntryPointFilterColumnType.VARCHAR = ExperimentsDatadogEntryPointFilterColumnType("varchar")
ExperimentsDatadogEntryPointFilterColumnType.INT = ExperimentsDatadogEntryPointFilterColumnType("int")
ExperimentsDatadogEntryPointFilterColumnType.DOUBLE = ExperimentsDatadogEntryPointFilterColumnType("double")
ExperimentsDatadogEntryPointFilterColumnType.BOOLEAN = ExperimentsDatadogEntryPointFilterColumnType("boolean")
ExperimentsDatadogEntryPointFilterColumnType.VARCHAR_ARRAY = ExperimentsDatadogEntryPointFilterColumnType(
    "varchar_array"
)
ExperimentsDatadogEntryPointFilterColumnType.INT_ARRAY = ExperimentsDatadogEntryPointFilterColumnType("int_array")
ExperimentsDatadogEntryPointFilterColumnType.DOUBLE_ARRAY = ExperimentsDatadogEntryPointFilterColumnType("double_array")
ExperimentsDatadogEntryPointFilterColumnType.RAW = ExperimentsDatadogEntryPointFilterColumnType("raw")
