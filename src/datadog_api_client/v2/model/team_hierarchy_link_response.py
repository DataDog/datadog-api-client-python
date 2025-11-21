# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_hierarchy_link import TeamHierarchyLink
    from datadog_api_client.v2.model.team_hierarchy_link_team import TeamHierarchyLinkTeam


class TeamHierarchyLinkResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_link import TeamHierarchyLink
        from datadog_api_client.v2.model.team_hierarchy_link_team import TeamHierarchyLinkTeam

        return {
            "data": (TeamHierarchyLink,),
            "included": ([TeamHierarchyLinkTeam],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[TeamHierarchyLink, UnsetType] = unset,
        included: Union[List[TeamHierarchyLinkTeam], UnsetType] = unset,
        **kwargs,
    ):
        """
        Team hierarchy link response

        :param data: Team hierarchy link
        :type data: TeamHierarchyLink, optional

        :param included: Included teams
        :type included: [TeamHierarchyLinkTeam], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
