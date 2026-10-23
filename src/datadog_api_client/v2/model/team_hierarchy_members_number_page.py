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
    from datadog_api_client.v2.model.team_hierarchy_members_number_page_type import TeamHierarchyMembersNumberPageType


class TeamHierarchyMembersNumberPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_members_number_page_type import (
            TeamHierarchyMembersNumberPageType,
        )

        return {
            "first_number": (int,),
            "last_number": (int, none_type),
            "next_number": (int, none_type),
            "number": (int,),
            "prev_number": (int, none_type),
            "size": (int,),
            "total": (int,),
            "type": (TeamHierarchyMembersNumberPageType,),
        }

    attribute_map = {
        "first_number": "first_number",
        "last_number": "last_number",
        "next_number": "next_number",
        "number": "number",
        "prev_number": "prev_number",
        "size": "size",
        "total": "total",
        "type": "type",
    }

    def __init__(
        self_,
        first_number: int,
        last_number: Union[int, none_type],
        next_number: Union[int, none_type],
        number: int,
        prev_number: Union[int, none_type],
        size: int,
        total: int,
        type: TeamHierarchyMembersNumberPageType,
        **kwargs,
    ):
        """
        Pagination metadata using number and size.

        :param first_number: First page number.
        :type first_number: int

        :param last_number: Last page number. Null when unavailable.
        :type last_number: int, none_type

        :param next_number: Next page number. Null when unavailable.
        :type next_number: int, none_type

        :param number: Current zero-based page number.
        :type number: int

        :param prev_number: Previous page number. Null when unavailable.
        :type prev_number: int, none_type

        :param size: Maximum number of members per page.
        :type size: int

        :param total: Total number of members matching the filters.
        :type total: int

        :param type: Pagination mode.
        :type type: TeamHierarchyMembersNumberPageType
        """
        super().__init__(kwargs)

        self_.first_number = first_number
        self_.last_number = last_number
        self_.next_number = next_number
        self_.number = number
        self_.prev_number = prev_number
        self_.size = size
        self_.total = total
        self_.type = type
