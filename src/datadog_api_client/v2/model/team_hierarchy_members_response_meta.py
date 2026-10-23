# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_hierarchy_members_page import TeamHierarchyMembersPage
    from datadog_api_client.v2.model.team_hierarchy_members_offset_page import TeamHierarchyMembersOffsetPage
    from datadog_api_client.v2.model.team_hierarchy_members_number_page import TeamHierarchyMembersNumberPage


class TeamHierarchyMembersResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_members_page import TeamHierarchyMembersPage

        return {
            "page": (TeamHierarchyMembersPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(
        self_,
        page: Union[TeamHierarchyMembersPage, TeamHierarchyMembersOffsetPage, TeamHierarchyMembersNumberPage],
        **kwargs,
    ):
        """
        Pagination metadata for the filtered members.

        :param page: Pagination metadata for the selected pagination mode.
        :type page: TeamHierarchyMembersPage
        """
        super().__init__(kwargs)

        self_.page = page
