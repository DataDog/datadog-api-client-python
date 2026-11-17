# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SegmentSortColumn(ModelSimple):
    """
    Column to sort segments by.

    :param value: Must be one of ["name", "description", "created_by", "created_at", "modified_by", "modified_at", "disabled_by", "disabled_at", "uuid"].
    :type value: str
    """

    allowed_values = {
        "name",
        "description",
        "created_by",
        "created_at",
        "modified_by",
        "modified_at",
        "disabled_by",
        "disabled_at",
        "uuid",
    }
    NAME: ClassVar["SegmentSortColumn"]
    DESCRIPTION: ClassVar["SegmentSortColumn"]
    CREATED_BY: ClassVar["SegmentSortColumn"]
    CREATED_AT: ClassVar["SegmentSortColumn"]
    MODIFIED_BY: ClassVar["SegmentSortColumn"]
    MODIFIED_AT: ClassVar["SegmentSortColumn"]
    DISABLED_BY: ClassVar["SegmentSortColumn"]
    DISABLED_AT: ClassVar["SegmentSortColumn"]
    UUID: ClassVar["SegmentSortColumn"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SegmentSortColumn.NAME = SegmentSortColumn("name")
SegmentSortColumn.DESCRIPTION = SegmentSortColumn("description")
SegmentSortColumn.CREATED_BY = SegmentSortColumn("created_by")
SegmentSortColumn.CREATED_AT = SegmentSortColumn("created_at")
SegmentSortColumn.MODIFIED_BY = SegmentSortColumn("modified_by")
SegmentSortColumn.MODIFIED_AT = SegmentSortColumn("modified_at")
SegmentSortColumn.DISABLED_BY = SegmentSortColumn("disabled_by")
SegmentSortColumn.DISABLED_AT = SegmentSortColumn("disabled_at")
SegmentSortColumn.UUID = SegmentSortColumn("uuid")
