# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_hierarchy_member_attributes import TeamHierarchyMemberAttributes
    from datadog_api_client.v2.model.team_hierarchy_member_relationships import TeamHierarchyMemberRelationships
    from datadog_api_client.v2.model.team_hierarchy_member_type import TeamHierarchyMemberType


class TeamHierarchyMember(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_member_attributes import TeamHierarchyMemberAttributes
        from datadog_api_client.v2.model.team_hierarchy_member_relationships import TeamHierarchyMemberRelationships
        from datadog_api_client.v2.model.team_hierarchy_member_type import TeamHierarchyMemberType

        return {
            "attributes": (TeamHierarchyMemberAttributes,),
            "id": (str,),
            "relationships": (TeamHierarchyMemberRelationships,),
            "type": (TeamHierarchyMemberType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TeamHierarchyMemberAttributes,
        id: str,
        relationships: TeamHierarchyMemberRelationships,
        type: TeamHierarchyMemberType,
        **kwargs,
    ):
        """
        A user relationship to the requested team.

        :param attributes: Membership attributes relative to the requested team.
        :type attributes: TeamHierarchyMemberAttributes

        :param id: Relationship identifier containing the team UUID and user UUID.
        :type id: str

        :param relationships: User and requested team linkage.
        :type relationships: TeamHierarchyMemberRelationships

        :param type: Team hierarchy membership resource type.
        :type type: TeamHierarchyMemberType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
