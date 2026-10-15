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
    from datadog_api_client.v2.model.team_hierarchy_member_team_attributes import TeamHierarchyMemberTeamAttributes
    from datadog_api_client.v2.model.team_hierarchy_member_team_type import TeamHierarchyMemberTeamType


class TeamHierarchyMemberTeam(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_member_team_attributes import TeamHierarchyMemberTeamAttributes
        from datadog_api_client.v2.model.team_hierarchy_member_team_type import TeamHierarchyMemberTeamType

        return {
            "attributes": (TeamHierarchyMemberTeamAttributes,),
            "id": (UUID,),
            "type": (TeamHierarchyMemberTeamType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: TeamHierarchyMemberTeamType,
        attributes: Union[TeamHierarchyMemberTeamAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The requested team, included at most once. Descendant teams are not included.

        :param attributes: Available attributes of the requested team.
        :type attributes: TeamHierarchyMemberTeamAttributes, optional

        :param id: UUID of the requested team.
        :type id: UUID

        :param type: Requested team resource type.
        :type type: TeamHierarchyMemberTeamType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
