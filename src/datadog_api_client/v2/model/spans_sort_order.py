# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SpansSortOrder(StringEnum):
    """
    The order to use, ascending or descending.

    :param value: Must be one of ["asc", "desc"].
    :type value: str
    """

    allowed_values = {
        "asc",
        "desc",
    }
    ASCENDING: ClassVar["SpansSortOrder"]
    DESCENDING: ClassVar["SpansSortOrder"]


SpansSortOrder.ASCENDING = SpansSortOrder("asc")
SpansSortOrder.DESCENDING = SpansSortOrder("desc")
