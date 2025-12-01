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
    from datadog_api_client.v2.model.team_hierarchy_link_create_team_relationship import (
        TeamHierarchyLinkCreateTeamRelationship,
    )


class TeamHierarchyLinkCreateRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_link_create_team_relationship import (
            TeamHierarchyLinkCreateTeamRelationship,
        )

        return {
            "parent_team": (TeamHierarchyLinkCreateTeamRelationship,),
            "sub_team": (TeamHierarchyLinkCreateTeamRelationship,),
        }

    attribute_map = {
        "parent_team": "parent_team",
        "sub_team": "sub_team",
    }

    def __init__(
        self_,
        parent_team: TeamHierarchyLinkCreateTeamRelationship,
        sub_team: TeamHierarchyLinkCreateTeamRelationship,
        **kwargs,
    ):
        """
        The related teams that will be connected by the team hierarchy link

        :param parent_team: Data about each team that will be connected by the team hierarchy link
        :type parent_team: TeamHierarchyLinkCreateTeamRelationship

        :param sub_team: Data about each team that will be connected by the team hierarchy link
        :type sub_team: TeamHierarchyLinkCreateTeamRelationship
        """
        super().__init__(kwargs)

        self_.parent_team = parent_team
        self_.sub_team = sub_team
