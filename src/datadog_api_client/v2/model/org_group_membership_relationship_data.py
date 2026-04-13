# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_group_membership_type import OrgGroupMembershipType


class OrgGroupMembershipRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_membership_type import OrgGroupMembershipType

        return {
            "id": (UUID,),
            "type": (OrgGroupMembershipType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: OrgGroupMembershipType, **kwargs):
        """
        A reference to an org group membership.

        :param id: The ID of the membership.
        :type id: UUID

        :param type: Org group memberships resource type.
        :type type: OrgGroupMembershipType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
