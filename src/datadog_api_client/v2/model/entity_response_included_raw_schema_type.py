# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityResponseIncludedRawSchemaType(ModelSimple):
    """
    Raw schema type.

    :param value: If omitted defaults to "rawSchema". Must be one of ["rawSchema"].
    :type value: str
    """

    allowed_values = {
        "rawSchema",
    }
    RAW_SCHEMA: ClassVar["EntityResponseIncludedRawSchemaType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityResponseIncludedRawSchemaType.RAW_SCHEMA = EntityResponseIncludedRawSchemaType("rawSchema")
