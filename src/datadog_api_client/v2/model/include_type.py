# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncludeType(ModelSimple):
    """
    supported include types.

    :param value: Must be one of ["schema", "raw_schema", "oncall", "incident", "relation"].
    :type value: str
    """

    allowed_values = {
        "schema",
        "raw_schema",
        "oncall",
        "incident",
        "relation",
    }
    SCHEMA: ClassVar["IncludeType"]
    RAW_SCHEMA: ClassVar["IncludeType"]
    ONCALL: ClassVar["IncludeType"]
    INCIDENT: ClassVar["IncludeType"]
    RELATION: ClassVar["IncludeType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncludeType.SCHEMA = IncludeType("schema")
IncludeType.RAW_SCHEMA = IncludeType("raw_schema")
IncludeType.ONCALL = IncludeType("oncall")
IncludeType.INCIDENT = IncludeType("incident")
IncludeType.RELATION = IncludeType("relation")
