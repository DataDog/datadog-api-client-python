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
    from datadog_api_client.v2.model.team_hierarchy_link_team import TeamHierarchyLinkTeam


class TeamHierarchyLinkTeamRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_link_team import TeamHierarchyLinkTeam

        return {
            "data": (TeamHierarchyLinkTeam,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TeamHierarchyLinkTeam, **kwargs):
        """
        Team hierarchy link team relationship

        :param data: Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.
        :type data: TeamHierarchyLinkTeam
        """
        super().__init__(kwargs)

        self_.data = data
