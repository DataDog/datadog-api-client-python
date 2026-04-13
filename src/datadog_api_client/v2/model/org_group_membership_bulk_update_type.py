# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupMembershipBulkUpdateType(ModelSimple):
    """
    Org group membership bulk update resource type.

    :param value: If omitted defaults to "org_group_membership_bulk_updates". Must be one of ["org_group_membership_bulk_updates"].
    :type value: str
    """

    allowed_values = {
        "org_group_membership_bulk_updates",
    }
    ORG_GROUP_MEMBERSHIP_BULK_UPDATES: ClassVar["OrgGroupMembershipBulkUpdateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupMembershipBulkUpdateType.ORG_GROUP_MEMBERSHIP_BULK_UPDATES = OrgGroupMembershipBulkUpdateType(
    "org_group_membership_bulk_updates"
)
