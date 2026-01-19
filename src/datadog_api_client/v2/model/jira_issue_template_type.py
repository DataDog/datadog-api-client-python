# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class JiraIssueTemplateType(ModelSimple):
    """
    Type identifier for Jira issue template resources

    :param value: If omitted defaults to "jira-issue-template". Must be one of ["jira-issue-template"].
    :type value: str
    """

    allowed_values = {
        "jira-issue-template",
    }
    JIRA_ISSUE_TEMPLATE: ClassVar["JiraIssueTemplateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


JiraIssueTemplateType.JIRA_ISSUE_TEMPLATE = JiraIssueTemplateType("jira-issue-template")
