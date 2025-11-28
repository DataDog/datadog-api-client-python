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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_hierarchy_link_attributes import TeamHierarchyLinkAttributes
    from datadog_api_client.v2.model.team_hierarchy_link_relationships import TeamHierarchyLinkRelationships
    from datadog_api_client.v2.model.team_hierarchy_link_type import TeamHierarchyLinkType


class TeamHierarchyLink(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_link_attributes import TeamHierarchyLinkAttributes
        from datadog_api_client.v2.model.team_hierarchy_link_relationships import TeamHierarchyLinkRelationships
        from datadog_api_client.v2.model.team_hierarchy_link_type import TeamHierarchyLinkType

        return {
            "attributes": (TeamHierarchyLinkAttributes,),
            "id": (str,),
            "relationships": (TeamHierarchyLinkRelationships,),
            "type": (TeamHierarchyLinkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TeamHierarchyLinkAttributes,
        id: str,
        type: TeamHierarchyLinkType,
        relationships: Union[TeamHierarchyLinkRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team hierarchy link

        :param attributes: Team hierarchy link attributes
        :type attributes: TeamHierarchyLinkAttributes

        :param id: The team hierarchy link's identifier
        :type id: str

        :param relationships: Team hierarchy link relationships
        :type relationships: TeamHierarchyLinkRelationships, optional

        :param type: Team hierarchy link type
        :type type: TeamHierarchyLinkType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
