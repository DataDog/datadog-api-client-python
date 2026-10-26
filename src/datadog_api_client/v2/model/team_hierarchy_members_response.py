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
    from datadog_api_client.v2.model.team_hierarchy_member import TeamHierarchyMember
    from datadog_api_client.v2.model.team_hierarchy_member_included import TeamHierarchyMemberIncluded
    from datadog_api_client.v2.model.team_hierarchy_members_response_links import TeamHierarchyMembersResponseLinks
    from datadog_api_client.v2.model.team_hierarchy_members_response_meta import TeamHierarchyMembersResponseMeta
    from datadog_api_client.v2.model.team_hierarchy_member_user import TeamHierarchyMemberUser
    from datadog_api_client.v2.model.team_hierarchy_member_team import TeamHierarchyMemberTeam


class TeamHierarchyMembersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_member import TeamHierarchyMember
        from datadog_api_client.v2.model.team_hierarchy_member_included import TeamHierarchyMemberIncluded
        from datadog_api_client.v2.model.team_hierarchy_members_response_links import TeamHierarchyMembersResponseLinks
        from datadog_api_client.v2.model.team_hierarchy_members_response_meta import TeamHierarchyMembersResponseMeta

        return {
            "data": ([TeamHierarchyMember],),
            "included": ([TeamHierarchyMemberIncluded],),
            "links": (TeamHierarchyMembersResponseLinks,),
            "meta": (TeamHierarchyMembersResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[TeamHierarchyMember],
        links: TeamHierarchyMembersResponseLinks,
        meta: TeamHierarchyMembersResponseMeta,
        included: Union[
            List[Union[TeamHierarchyMemberIncluded, TeamHierarchyMemberUser, TeamHierarchyMemberTeam]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Direct and inherited members of the requested team.

        :param data: Membership relationships for users who belong to the requested team or inherit membership through its descendant teams. Each user appears once, even if they belong to multiple teams in the hierarchy. Each relationship identifies the user and requested team, and indicates whether the user is a direct member of the requested team.
        :type data: [TeamHierarchyMember]

        :param included: Requested users and the team. May be absent when the result is empty, even if requested.
        :type included: [TeamHierarchyMemberIncluded], optional

        :param links: Page navigation links. Unavailable links are omitted.
        :type links: TeamHierarchyMembersResponseLinks

        :param meta: Pagination metadata for the filtered members.
        :type meta: TeamHierarchyMembersResponseMeta
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
        self_.links = links
        self_.meta = meta
