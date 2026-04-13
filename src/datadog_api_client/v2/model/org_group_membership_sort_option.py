# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupMembershipSortOption(ModelSimple):
    """
    Field to sort memberships by.

    :param value: If omitted defaults to "uuid". Must be one of ["name", "-name", "uuid", "-uuid"].
    :type value: str
    """

    allowed_values = {
        "name",
        "-name",
        "uuid",
        "-uuid",
    }
    NAME: ClassVar["OrgGroupMembershipSortOption"]
    MINUS_NAME: ClassVar["OrgGroupMembershipSortOption"]
    UUID: ClassVar["OrgGroupMembershipSortOption"]
    MINUS_UUID: ClassVar["OrgGroupMembershipSortOption"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupMembershipSortOption.NAME = OrgGroupMembershipSortOption("name")
OrgGroupMembershipSortOption.MINUS_NAME = OrgGroupMembershipSortOption("-name")
OrgGroupMembershipSortOption.UUID = OrgGroupMembershipSortOption("uuid")
OrgGroupMembershipSortOption.MINUS_UUID = OrgGroupMembershipSortOption("-uuid")
