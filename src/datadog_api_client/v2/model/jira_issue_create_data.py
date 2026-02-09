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
    from datadog_api_client.v2.model.jira_issue_create_attributes import JiraIssueCreateAttributes
    from datadog_api_client.v2.model.jira_issue_resource_type import JiraIssueResourceType


class JiraIssueCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_create_attributes import JiraIssueCreateAttributes
        from datadog_api_client.v2.model.jira_issue_resource_type import JiraIssueResourceType

        return {
            "attributes": (JiraIssueCreateAttributes,),
            "type": (JiraIssueResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: JiraIssueCreateAttributes, type: JiraIssueResourceType, **kwargs):
        """
        Jira issue creation data

        :param attributes: Jira issue creation attributes
        :type attributes: JiraIssueCreateAttributes

        :param type: Jira issue resource type
        :type type: JiraIssueResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
