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
    from datadog_api_client.v2.model.issues_search_result_issue_relationship import IssuesSearchResultIssueRelationship


class IssuesSearchResultRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issues_search_result_issue_relationship import (
            IssuesSearchResultIssueRelationship,
        )

        return {
            "issue": (IssuesSearchResultIssueRelationship,),
        }

    attribute_map = {
        "issue": "issue",
    }

    def __init__(self_, issue: Union[IssuesSearchResultIssueRelationship, UnsetType] = unset, **kwargs):
        """
        Relationships between the search result and other resources.

        :param issue: Relationship between the search result and the corresponding issue.
        :type issue: IssuesSearchResultIssueRelationship, optional
        """
        if issue is not unset:
            kwargs["issue"] = issue
        super().__init__(kwargs)
