# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_group_membership_attributes import OrgGroupMembershipAttributes
    from datadog_api_client.v2.model.org_group_membership_relationships import OrgGroupMembershipRelationships
    from datadog_api_client.v2.model.org_group_membership_type import OrgGroupMembershipType


class OrgGroupMembershipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_membership_attributes import OrgGroupMembershipAttributes
        from datadog_api_client.v2.model.org_group_membership_relationships import OrgGroupMembershipRelationships
        from datadog_api_client.v2.model.org_group_membership_type import OrgGroupMembershipType

        return {
            "attributes": (OrgGroupMembershipAttributes,),
            "id": (UUID,),
            "relationships": (OrgGroupMembershipRelationships,),
            "type": (OrgGroupMembershipType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgGroupMembershipAttributes,
        id: UUID,
        type: OrgGroupMembershipType,
        relationships: Union[OrgGroupMembershipRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        An org group membership resource.

        :param attributes: Attributes of an org group membership.
        :type attributes: OrgGroupMembershipAttributes

        :param id: The ID of the org group membership.
        :type id: UUID

        :param relationships: Relationships of an org group membership.
        :type relationships: OrgGroupMembershipRelationships, optional

        :param type: Org group memberships resource type.
        :type type: OrgGroupMembershipType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
