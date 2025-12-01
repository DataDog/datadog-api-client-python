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
    from datadog_api_client.v2.model.team_hierarchy_link_team_attributes import TeamHierarchyLinkTeamAttributes
    from datadog_api_client.v2.model.team_type import TeamType


class TeamHierarchyLinkTeam(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_link_team_attributes import TeamHierarchyLinkTeamAttributes
        from datadog_api_client.v2.model.team_type import TeamType

        return {
            "attributes": (TeamHierarchyLinkTeamAttributes,),
            "id": (str,),
            "type": (TeamType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, id: str, type: TeamType, attributes: Union[TeamHierarchyLinkTeamAttributes, UnsetType] = unset, **kwargs
    ):
        """
        Team hierarchy links connect different teams. This represents team objects that are connected by the team hierarchy link.

        :param attributes: Team hierarchy links connect different teams. This represents attributes from teams that are connected by the team hierarchy link.
        :type attributes: TeamHierarchyLinkTeamAttributes, optional

        :param id: The team's identifier
        :type id: str

        :param type: Team type
        :type type: TeamType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
