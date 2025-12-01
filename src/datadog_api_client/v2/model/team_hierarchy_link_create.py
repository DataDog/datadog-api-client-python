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
    from datadog_api_client.v2.model.team_hierarchy_link_create_relationships import (
        TeamHierarchyLinkCreateRelationships,
    )
    from datadog_api_client.v2.model.team_hierarchy_link_type import TeamHierarchyLinkType


class TeamHierarchyLinkCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_link_create_relationships import (
            TeamHierarchyLinkCreateRelationships,
        )
        from datadog_api_client.v2.model.team_hierarchy_link_type import TeamHierarchyLinkType

        return {
            "relationships": (TeamHierarchyLinkCreateRelationships,),
            "type": (TeamHierarchyLinkType,),
        }

    attribute_map = {
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self_, relationships: TeamHierarchyLinkCreateRelationships, type: TeamHierarchyLinkType, **kwargs):
        """
        Data provided when creating a team hierarchy link

        :param relationships: The related teams that will be connected by the team hierarchy link
        :type relationships: TeamHierarchyLinkCreateRelationships

        :param type: Team hierarchy link type
        :type type: TeamHierarchyLinkType
        """
        super().__init__(kwargs)

        self_.relationships = relationships
        self_.type = type
