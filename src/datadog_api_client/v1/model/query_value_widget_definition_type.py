# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class QueryValueWidgetDefinitionType(StringEnum):
    """
    Type of the query value widget.

    :param value: If omitted defaults to "query_value". Must be one of ["query_value"].
    :type value: str
    """

    allowed_values = {
        "query_value",
    }
    QUERY_VALUE: ClassVar["QueryValueWidgetDefinitionType"]


QueryValueWidgetDefinitionType.QUERY_VALUE = QueryValueWidgetDefinitionType("query_value")
