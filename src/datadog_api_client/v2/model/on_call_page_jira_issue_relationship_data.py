# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_page_jira_issue_type import OnCallPageJiraIssueType


class OnCallPageJiraIssueRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_jira_issue_type import OnCallPageJiraIssueType

        return {
            "id": (str,),
            "type": (OnCallPageJiraIssueType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: OnCallPageJiraIssueType, **kwargs):
        """
        Reference to a Jira issue.

        :param id: The ID of the Jira issue, in the form ``<account_id>:<issue_id>``.
        :type id: str

        :param type: Jira issue resource type.
        :type type: OnCallPageJiraIssueType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
