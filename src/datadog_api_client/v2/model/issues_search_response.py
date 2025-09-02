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
    from datadog_api_client.v2.model.issues_search_result import IssuesSearchResult
    from datadog_api_client.v2.model.issues_search_result_included import IssuesSearchResultIncluded
    from datadog_api_client.v2.model.issue import Issue
    from datadog_api_client.v2.model.case import Case
    from datadog_api_client.v2.model.issue_user import IssueUser
    from datadog_api_client.v2.model.issue_team import IssueTeam


class IssuesSearchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issues_search_result import IssuesSearchResult
        from datadog_api_client.v2.model.issues_search_result_included import IssuesSearchResultIncluded

        return {
            "data": ([IssuesSearchResult],),
            "included": ([IssuesSearchResultIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[List[IssuesSearchResult], UnsetType] = unset,
        included: Union[List[Union[IssuesSearchResultIncluded, Issue, Case, IssueUser, IssueTeam]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Search issues response payload.

        :param data: Array of results matching the search query.
        :type data: [IssuesSearchResult], optional

        :param included: Array of resources related to the search results.
        :type included: [IssuesSearchResultIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
