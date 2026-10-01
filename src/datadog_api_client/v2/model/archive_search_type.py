# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ArchiveSearchType(ModelSimple):
    """
    Archive Search resource type.

    :param value: If omitted defaults to "archive_search". Must be one of ["archive_search"].
    :type value: str
    """

    allowed_values = {
        "archive_search",
    }
    ARCHIVE_SEARCH: ClassVar["ArchiveSearchType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ArchiveSearchType.ARCHIVE_SEARCH = ArchiveSearchType("archive_search")
