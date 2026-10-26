# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamHierarchyMembersNumberPageType(ModelSimple):
    """
    Pagination mode.

    :param value: If omitted defaults to "number_size". Must be one of ["number_size"].
    :type value: str
    """

    allowed_values = {
        "number_size",
    }
    NUMBER_SIZE: ClassVar["TeamHierarchyMembersNumberPageType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamHierarchyMembersNumberPageType.NUMBER_SIZE = TeamHierarchyMembersNumberPageType("number_size")
