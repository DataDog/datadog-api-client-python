# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ListStreamQueryVersion(ModelSimple):
    """
    Version of the query for the logs transaction stream widget. When omitted, v1 query behavior is
        preserved. Set to `sequential_query` to use v2 behavior. **This feature is in Preview.**

    :param value: If omitted defaults to "sequential_query". Must be one of ["sequential_query"].
    :type value: str
    """

    allowed_values = {
        "sequential_query",
    }
    SEQUENTIAL_QUERY: ClassVar["ListStreamQueryVersion"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ListStreamQueryVersion.SEQUENTIAL_QUERY = ListStreamQueryVersion("sequential_query")
