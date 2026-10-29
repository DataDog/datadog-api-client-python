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
    from datadog_api_client.v2.model.on_call_page_jira_issue_relationship_data import (
        OnCallPageJiraIssueRelationshipData,
    )


class OnCallPageJiraIssueRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_jira_issue_relationship_data import (
            OnCallPageJiraIssueRelationshipData,
        )

        return {
            "data": (OnCallPageJiraIssueRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[OnCallPageJiraIssueRelationshipData, UnsetType] = unset, **kwargs):
        """
        The Jira issue linked to the Page.

        :param data: Reference to a Jira issue.
        :type data: OnCallPageJiraIssueRelationshipData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
