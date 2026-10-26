# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_hierarchy_members_offset_page_type import TeamHierarchyMembersOffsetPageType


class TeamHierarchyMembersOffsetPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_members_offset_page_type import (
            TeamHierarchyMembersOffsetPageType,
        )

        return {
            "first_offset": (int,),
            "last_offset": (int, none_type),
            "limit": (int,),
            "next_offset": (int, none_type),
            "offset": (int,),
            "prev_offset": (int, none_type),
            "total": (int,),
            "type": (TeamHierarchyMembersOffsetPageType,),
        }

    attribute_map = {
        "first_offset": "first_offset",
        "last_offset": "last_offset",
        "limit": "limit",
        "next_offset": "next_offset",
        "offset": "offset",
        "prev_offset": "prev_offset",
        "total": "total",
        "type": "type",
    }

    def __init__(
        self_,
        first_offset: int,
        last_offset: Union[int, none_type],
        limit: int,
        next_offset: Union[int, none_type],
        offset: int,
        prev_offset: Union[int, none_type],
        total: int,
        type: TeamHierarchyMembersOffsetPageType,
        **kwargs,
    ):
        """
        Pagination metadata using offset and limit.

        :param first_offset: First offset.
        :type first_offset: int

        :param last_offset: Last offset. Null when unavailable.
        :type last_offset: int, none_type

        :param limit: Maximum number of members per page.
        :type limit: int

        :param next_offset: Next offset. Null when unavailable.
        :type next_offset: int, none_type

        :param offset: Current offset.
        :type offset: int

        :param prev_offset: Previous offset. Null when unavailable.
        :type prev_offset: int, none_type

        :param total: Total number of members matching the filters.
        :type total: int

        :param type: Pagination mode.
        :type type: TeamHierarchyMembersOffsetPageType
        """
        super().__init__(kwargs)

        self_.first_offset = first_offset
        self_.last_offset = last_offset
        self_.limit = limit
        self_.next_offset = next_offset
        self_.offset = offset
        self_.prev_offset = prev_offset
        self_.total = total
        self_.type = type
