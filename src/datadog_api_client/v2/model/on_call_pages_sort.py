# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPagesSort(ModelSimple):
    """
    Sorting options for Pages. Prefix a field with `-` to sort in descending order.

    :param value: If omitted defaults to "created_at". Must be one of ["created_at", "-created_at", "modified_at", "-modified_at", "status", "-status", "priority", "-priority"].
    :type value: str
    """

    allowed_values = {
        "created_at",
        "-created_at",
        "modified_at",
        "-modified_at",
        "status",
        "-status",
        "priority",
        "-priority",
    }
    CREATED_AT_ASCENDING: ClassVar["OnCallPagesSort"]
    CREATED_AT_DESCENDING: ClassVar["OnCallPagesSort"]
    MODIFIED_AT_ASCENDING: ClassVar["OnCallPagesSort"]
    MODIFIED_AT_DESCENDING: ClassVar["OnCallPagesSort"]
    STATUS_ASCENDING: ClassVar["OnCallPagesSort"]
    STATUS_DESCENDING: ClassVar["OnCallPagesSort"]
    PRIORITY_ASCENDING: ClassVar["OnCallPagesSort"]
    PRIORITY_DESCENDING: ClassVar["OnCallPagesSort"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPagesSort.CREATED_AT_ASCENDING = OnCallPagesSort("created_at")
OnCallPagesSort.CREATED_AT_DESCENDING = OnCallPagesSort("-created_at")
OnCallPagesSort.MODIFIED_AT_ASCENDING = OnCallPagesSort("modified_at")
OnCallPagesSort.MODIFIED_AT_DESCENDING = OnCallPagesSort("-modified_at")
OnCallPagesSort.STATUS_ASCENDING = OnCallPagesSort("status")
OnCallPagesSort.STATUS_DESCENDING = OnCallPagesSort("-status")
OnCallPagesSort.PRIORITY_ASCENDING = OnCallPagesSort("priority")
OnCallPagesSort.PRIORITY_DESCENDING = OnCallPagesSort("-priority")
