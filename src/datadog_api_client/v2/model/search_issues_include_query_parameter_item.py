# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SearchIssuesIncludeQueryParameterItem(ModelSimple):
    """
    Relationship object that should be included in the search response.

    :param value: Must be one of ["issue", "issue.assignee", "issue.case", "issue.team_owners"].
    :type value: str
    """

    allowed_values = {
        "issue",
        "issue.assignee",
        "issue.case",
        "issue.team_owners",
    }
    ISSUE: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_ASSIGNEE: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_CASE: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_TEAM_OWNERS: ClassVar["SearchIssuesIncludeQueryParameterItem"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SearchIssuesIncludeQueryParameterItem.ISSUE = SearchIssuesIncludeQueryParameterItem("issue")
SearchIssuesIncludeQueryParameterItem.ISSUE_ASSIGNEE = SearchIssuesIncludeQueryParameterItem("issue.assignee")
SearchIssuesIncludeQueryParameterItem.ISSUE_CASE = SearchIssuesIncludeQueryParameterItem("issue.case")
SearchIssuesIncludeQueryParameterItem.ISSUE_TEAM_OWNERS = SearchIssuesIncludeQueryParameterItem("issue.team_owners")
