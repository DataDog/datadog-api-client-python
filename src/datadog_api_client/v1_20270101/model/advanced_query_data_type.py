# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AdvancedQueryDataType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["string", "group", "inet", "int64", "float64", "timestamp", "date", "interval", "bool", "json", "hstore", "array<string>", "array<int64>", "array<float64>", "array<timestamp>", "array<interval>", "array<bool>", "array<json>"].
    :type value: str
    """

    allowed_values = {
        "string",
        "group",
        "inet",
        "int64",
        "float64",
        "timestamp",
        "date",
        "interval",
        "bool",
        "json",
        "hstore",
        "array<string>",
        "array<int64>",
        "array<float64>",
        "array<timestamp>",
        "array<interval>",
        "array<bool>",
        "array<json>",
    }
    STRING: ClassVar["AdvancedQueryDataType"]
    GROUP: ClassVar["AdvancedQueryDataType"]
    INET: ClassVar["AdvancedQueryDataType"]
    INT64: ClassVar["AdvancedQueryDataType"]
    FLOAT64: ClassVar["AdvancedQueryDataType"]
    TIMESTAMP: ClassVar["AdvancedQueryDataType"]
    DATE: ClassVar["AdvancedQueryDataType"]
    INTERVAL: ClassVar["AdvancedQueryDataType"]
    BOOL: ClassVar["AdvancedQueryDataType"]
    JSON: ClassVar["AdvancedQueryDataType"]
    HSTORE: ClassVar["AdvancedQueryDataType"]
    ARRAYLTSTRINGGT: ClassVar["AdvancedQueryDataType"]
    ARRAYLTINT64GT: ClassVar["AdvancedQueryDataType"]
    ARRAYLTFLOAT64GT: ClassVar["AdvancedQueryDataType"]
    ARRAYLTTIMESTAMPGT: ClassVar["AdvancedQueryDataType"]
    ARRAYLTINTERVALGT: ClassVar["AdvancedQueryDataType"]
    ARRAYLTBOOLGT: ClassVar["AdvancedQueryDataType"]
    ARRAYLTJSONGT: ClassVar["AdvancedQueryDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AdvancedQueryDataType.STRING = AdvancedQueryDataType("string")
AdvancedQueryDataType.GROUP = AdvancedQueryDataType("group")
AdvancedQueryDataType.INET = AdvancedQueryDataType("inet")
AdvancedQueryDataType.INT64 = AdvancedQueryDataType("int64")
AdvancedQueryDataType.FLOAT64 = AdvancedQueryDataType("float64")
AdvancedQueryDataType.TIMESTAMP = AdvancedQueryDataType("timestamp")
AdvancedQueryDataType.DATE = AdvancedQueryDataType("date")
AdvancedQueryDataType.INTERVAL = AdvancedQueryDataType("interval")
AdvancedQueryDataType.BOOL = AdvancedQueryDataType("bool")
AdvancedQueryDataType.JSON = AdvancedQueryDataType("json")
AdvancedQueryDataType.HSTORE = AdvancedQueryDataType("hstore")
AdvancedQueryDataType.ARRAYLTSTRINGGT = AdvancedQueryDataType("array<string>")
AdvancedQueryDataType.ARRAYLTINT64GT = AdvancedQueryDataType("array<int64>")
AdvancedQueryDataType.ARRAYLTFLOAT64GT = AdvancedQueryDataType("array<float64>")
AdvancedQueryDataType.ARRAYLTTIMESTAMPGT = AdvancedQueryDataType("array<timestamp>")
AdvancedQueryDataType.ARRAYLTINTERVALGT = AdvancedQueryDataType("array<interval>")
AdvancedQueryDataType.ARRAYLTBOOLGT = AdvancedQueryDataType("array<bool>")
AdvancedQueryDataType.ARRAYLTJSONGT = AdvancedQueryDataType("array<json>")
