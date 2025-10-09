# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ReferenceTableSortType(ModelSimple):
    """
    Sort field and direction for reference tables. Use field name for ascending, prefix with "-" for descending.

    :param value: If omitted defaults to "-updated_at". Must be one of ["updated_at", "table_name", "status", "-updated_at", "-table_name", "-status"].
    :type value: str
    """

    allowed_values = {
        "updated_at",
        "table_name",
        "status",
        "-updated_at",
        "-table_name",
        "-status",
    }
    UPDATED_AT: ClassVar["ReferenceTableSortType"]
    TABLE_NAME: ClassVar["ReferenceTableSortType"]
    STATUS: ClassVar["ReferenceTableSortType"]
    MINUS_UPDATED_AT: ClassVar["ReferenceTableSortType"]
    MINUS_TABLE_NAME: ClassVar["ReferenceTableSortType"]
    MINUS_STATUS: ClassVar["ReferenceTableSortType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ReferenceTableSortType.UPDATED_AT = ReferenceTableSortType("updated_at")
ReferenceTableSortType.TABLE_NAME = ReferenceTableSortType("table_name")
ReferenceTableSortType.STATUS = ReferenceTableSortType("status")
ReferenceTableSortType.MINUS_UPDATED_AT = ReferenceTableSortType("-updated_at")
ReferenceTableSortType.MINUS_TABLE_NAME = ReferenceTableSortType("-table_name")
ReferenceTableSortType.MINUS_STATUS = ReferenceTableSortType("-status")
