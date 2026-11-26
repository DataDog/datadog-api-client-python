# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class StructuredAnalysisCastTargetType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["string", "int64", "float64", "timestamp"].
    :type value: str
    """

    allowed_values = {
        "string",
        "int64",
        "float64",
        "timestamp",
    }
    STRING: ClassVar["StructuredAnalysisCastTargetType"]
    INT64: ClassVar["StructuredAnalysisCastTargetType"]
    FLOAT64: ClassVar["StructuredAnalysisCastTargetType"]
    TIMESTAMP: ClassVar["StructuredAnalysisCastTargetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


StructuredAnalysisCastTargetType.STRING = StructuredAnalysisCastTargetType("string")
StructuredAnalysisCastTargetType.INT64 = StructuredAnalysisCastTargetType("int64")
StructuredAnalysisCastTargetType.FLOAT64 = StructuredAnalysisCastTargetType("float64")
StructuredAnalysisCastTargetType.TIMESTAMP = StructuredAnalysisCastTargetType("timestamp")
