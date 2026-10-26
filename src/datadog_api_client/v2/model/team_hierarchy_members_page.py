# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TeamHierarchyMembersPage(ModelComposed):
    def __init__(self, **kwargs):
        """
        Pagination metadata for the selected pagination mode.

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
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.team_hierarchy_members_offset_page import TeamHierarchyMembersOffsetPage
        from datadog_api_client.v2.model.team_hierarchy_members_number_page import TeamHierarchyMembersNumberPage

        return {
            "oneOf": [
                TeamHierarchyMembersOffsetPage,
                TeamHierarchyMembersNumberPage,
            ],
        }
