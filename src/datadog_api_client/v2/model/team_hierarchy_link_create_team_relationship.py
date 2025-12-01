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
    from datadog_api_client.v2.model.team_hierarchy_link_create_team import TeamHierarchyLinkCreateTeam


class TeamHierarchyLinkCreateTeamRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_link_create_team import TeamHierarchyLinkCreateTeam

        return {
            "data": (TeamHierarchyLinkCreateTeam,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TeamHierarchyLinkCreateTeam, **kwargs):
        """
        Data about each team that will be connected by the team hierarchy link

        :param data: This schema defines the attributes about each team that has to be provided when creating a team hierarchy link
        :type data: TeamHierarchyLinkCreateTeam
        """
        super().__init__(kwargs)

        self_.data = data
