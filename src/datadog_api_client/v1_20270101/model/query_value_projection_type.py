# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class QueryValueProjectionType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "query_value". Must be one of ["query_value"].
    :type value: str
    """

    allowed_values = {
        "query_value",
    }
    QUERY_VALUE: ClassVar["QueryValueProjectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


QueryValueProjectionType.QUERY_VALUE = QueryValueProjectionType("query_value")
