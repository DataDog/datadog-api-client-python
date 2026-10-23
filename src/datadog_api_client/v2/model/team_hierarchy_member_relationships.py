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
    from datadog_api_client.v2.model.team_hierarchy_member_team_relationship import TeamHierarchyMemberTeamRelationship
    from datadog_api_client.v2.model.team_hierarchy_member_user_relationship import TeamHierarchyMemberUserRelationship


class TeamHierarchyMemberRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_member_team_relationship import (
            TeamHierarchyMemberTeamRelationship,
        )
        from datadog_api_client.v2.model.team_hierarchy_member_user_relationship import (
            TeamHierarchyMemberUserRelationship,
        )

        return {
            "team": (TeamHierarchyMemberTeamRelationship,),
            "user": (TeamHierarchyMemberUserRelationship,),
        }

    attribute_map = {
        "team": "team",
        "user": "user",
    }

    def __init__(self_, team: TeamHierarchyMemberTeamRelationship, user: TeamHierarchyMemberUserRelationship, **kwargs):
        """
        User and requested team linkage.

        :param team: Linkage to the requested team.
        :type team: TeamHierarchyMemberTeamRelationship

        :param user: Linkage to the user.
        :type user: TeamHierarchyMemberUserRelationship
        """
        super().__init__(kwargs)

        self_.team = team
        self_.user = user
