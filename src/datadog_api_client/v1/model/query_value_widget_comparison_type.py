# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class QueryValueWidgetComparisonType(ModelSimple):
    """
    How the delta is expressed: `absolute` (raw difference), `relative` (percentage), or `both`.

    :param value: If omitted defaults to "absolute". Must be one of ["absolute", "relative", "both"].
    :type value: str
    """

    allowed_values = {
        "absolute",
        "relative",
        "both",
    }
    ABSOLUTE: ClassVar["QueryValueWidgetComparisonType"]
    RELATIVE: ClassVar["QueryValueWidgetComparisonType"]
    BOTH: ClassVar["QueryValueWidgetComparisonType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


QueryValueWidgetComparisonType.ABSOLUTE = QueryValueWidgetComparisonType("absolute")
QueryValueWidgetComparisonType.RELATIVE = QueryValueWidgetComparisonType("relative")
QueryValueWidgetComparisonType.BOTH = QueryValueWidgetComparisonType("both")
