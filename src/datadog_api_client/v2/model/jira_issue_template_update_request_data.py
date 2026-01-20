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
    from datadog_api_client.v2.model.jira_issue_template_update_request_attributes import (
        JiraIssueTemplateUpdateRequestAttributes,
    )
    from datadog_api_client.v2.model.jira_issue_template_type import JiraIssueTemplateType


class JiraIssueTemplateUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_template_update_request_attributes import (
            JiraIssueTemplateUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.jira_issue_template_type import JiraIssueTemplateType

        return {
            "attributes": (JiraIssueTemplateUpdateRequestAttributes,),
            "type": (JiraIssueTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: JiraIssueTemplateUpdateRequestAttributes, type: JiraIssueTemplateType, **kwargs):
        """
        Data object for updating a Jira issue template

        :param attributes: Attributes for updating a Jira issue template
        :type attributes: JiraIssueTemplateUpdateRequestAttributes

        :param type: Type identifier for Jira issue template resources
        :type type: JiraIssueTemplateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
