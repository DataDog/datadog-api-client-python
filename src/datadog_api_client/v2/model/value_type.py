# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ValueType(ModelSimple):
    """
    The type of values for the feature flag variants.

    :param value: Must be one of ["BOOLEAN", "INTEGER", "NUMERIC", "STRING", "JSON"].
    :type value: str
    """

    allowed_values = {
        "BOOLEAN",
        "INTEGER",
        "NUMERIC",
        "STRING",
        "JSON",
    }
    BOOLEAN: ClassVar["ValueType"]
    INTEGER: ClassVar["ValueType"]
    NUMERIC: ClassVar["ValueType"]
    STRING: ClassVar["ValueType"]
    JSON: ClassVar["ValueType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ValueType.BOOLEAN = ValueType("BOOLEAN")
ValueType.INTEGER = ValueType("INTEGER")
ValueType.NUMERIC = ValueType("NUMERIC")
ValueType.STRING = ValueType("STRING")
ValueType.JSON = ValueType("JSON")
