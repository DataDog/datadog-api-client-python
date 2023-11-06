# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class QuerySortOrder(StringEnum):
    """
    Direction of sort.

    :param value: If omitted defaults to "desc". Must be one of ["asc", "desc"].
    :type value: str
    """

    allowed_values = {
        "asc",
        "desc",
    }
    ASC: ClassVar["QuerySortOrder"]
    DESC: ClassVar["QuerySortOrder"]


QuerySortOrder.ASC = QuerySortOrder("asc")
QuerySortOrder.DESC = QuerySortOrder("desc")
