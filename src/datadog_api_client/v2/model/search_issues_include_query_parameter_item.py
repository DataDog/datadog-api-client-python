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

    :param value: Must be one of ["issue", "issue.assignee", "issue.bits_investigation", "issue.case", "issue.impacted_sessions", "issue.impacted_users", "issue.pull_requests", "issue.team_owners", "issue.watches"].
    :type value: str
    """

    allowed_values = {
        "issue",
        "issue.assignee",
        "issue.bits_investigation",
        "issue.case",
        "issue.impacted_sessions",
        "issue.impacted_users",
        "issue.pull_requests",
        "issue.team_owners",
        "issue.watches",
    }
    ISSUE: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_ASSIGNEE: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_BITS_INVESTIGATION: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_CASE: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_IMPACTED_SESSIONS: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_IMPACTED_USERS: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_PULL_REQUESTS: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_TEAM_OWNERS: ClassVar["SearchIssuesIncludeQueryParameterItem"]
    ISSUE_WATCHES: ClassVar["SearchIssuesIncludeQueryParameterItem"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SearchIssuesIncludeQueryParameterItem.ISSUE = SearchIssuesIncludeQueryParameterItem("issue")
SearchIssuesIncludeQueryParameterItem.ISSUE_ASSIGNEE = SearchIssuesIncludeQueryParameterItem("issue.assignee")
SearchIssuesIncludeQueryParameterItem.ISSUE_BITS_INVESTIGATION = SearchIssuesIncludeQueryParameterItem(
    "issue.bits_investigation"
)
SearchIssuesIncludeQueryParameterItem.ISSUE_CASE = SearchIssuesIncludeQueryParameterItem("issue.case")
SearchIssuesIncludeQueryParameterItem.ISSUE_IMPACTED_SESSIONS = SearchIssuesIncludeQueryParameterItem(
    "issue.impacted_sessions"
)
SearchIssuesIncludeQueryParameterItem.ISSUE_IMPACTED_USERS = SearchIssuesIncludeQueryParameterItem(
    "issue.impacted_users"
)
SearchIssuesIncludeQueryParameterItem.ISSUE_PULL_REQUESTS = SearchIssuesIncludeQueryParameterItem("issue.pull_requests")
SearchIssuesIncludeQueryParameterItem.ISSUE_TEAM_OWNERS = SearchIssuesIncludeQueryParameterItem("issue.team_owners")
SearchIssuesIncludeQueryParameterItem.ISSUE_WATCHES = SearchIssuesIncludeQueryParameterItem("issue.watches")
