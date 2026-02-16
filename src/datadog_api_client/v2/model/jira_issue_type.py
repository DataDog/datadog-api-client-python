# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class JiraIssueType(ModelSimple):
    """
    Jira issue resource type.

    :param value: If omitted defaults to "jira_issue". Must be one of ["jira_issue"].
    :type value: str
    """

    allowed_values = {
        "jira_issue",
    }
    JIRA_ISSUE: ClassVar["JiraIssueType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


JiraIssueType.JIRA_ISSUE = JiraIssueType("jira_issue")
