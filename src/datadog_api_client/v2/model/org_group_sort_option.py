# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupSortOption(ModelSimple):
    """
    Field to sort org groups by.

    :param value: If omitted defaults to "uuid". Must be one of ["name", "-name", "uuid", "-uuid"].
    :type value: str
    """

    allowed_values = {
        "name",
        "-name",
        "uuid",
        "-uuid",
    }
    NAME: ClassVar["OrgGroupSortOption"]
    MINUS_NAME: ClassVar["OrgGroupSortOption"]
    UUID: ClassVar["OrgGroupSortOption"]
    MINUS_UUID: ClassVar["OrgGroupSortOption"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupSortOption.NAME = OrgGroupSortOption("name")
OrgGroupSortOption.MINUS_NAME = OrgGroupSortOption("-name")
OrgGroupSortOption.UUID = OrgGroupSortOption("uuid")
OrgGroupSortOption.MINUS_UUID = OrgGroupSortOption("-uuid")
