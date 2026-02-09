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
    from datadog_api_client.v2.model.jira_issue_link_attributes import JiraIssueLinkAttributes
    from datadog_api_client.v2.model.jira_issue_resource_type import JiraIssueResourceType


class JiraIssueLinkData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_link_attributes import JiraIssueLinkAttributes
        from datadog_api_client.v2.model.jira_issue_resource_type import JiraIssueResourceType

        return {
            "attributes": (JiraIssueLinkAttributes,),
            "type": (JiraIssueResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: JiraIssueLinkAttributes, type: JiraIssueResourceType, **kwargs):
        """
        Jira issue link data

        :param attributes: Jira issue link attributes
        :type attributes: JiraIssueLinkAttributes

        :param type: Jira issue resource type
        :type type: JiraIssueResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
