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
    from datadog_api_client.v2.model.team_hierarchy_link_team_relationship import TeamHierarchyLinkTeamRelationship


class TeamHierarchyLinkRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_link_team_relationship import TeamHierarchyLinkTeamRelationship

        return {
            "parent_team": (TeamHierarchyLinkTeamRelationship,),
            "sub_team": (TeamHierarchyLinkTeamRelationship,),
        }

    attribute_map = {
        "parent_team": "parent_team",
        "sub_team": "sub_team",
    }

    def __init__(
        self_, parent_team: TeamHierarchyLinkTeamRelationship, sub_team: TeamHierarchyLinkTeamRelationship, **kwargs
    ):
        """
        Team hierarchy link relationships

        :param parent_team: Team hierarchy link team relationship
        :type parent_team: TeamHierarchyLinkTeamRelationship

        :param sub_team: Team hierarchy link team relationship
        :type sub_team: TeamHierarchyLinkTeamRelationship
        """
        super().__init__(kwargs)

        self_.parent_team = parent_team
        self_.sub_team = sub_team
