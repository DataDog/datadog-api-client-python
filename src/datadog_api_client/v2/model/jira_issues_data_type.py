# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class JiraIssuesDataType(ModelSimple):
    """
    Jira issues resource type.

    :param value: If omitted defaults to "jira_issues". Must be one of ["jira_issues"].
    :type value: str
    """

    allowed_values = {
        "jira_issues",
    }
    JIRA_ISSUES: ClassVar["JiraIssuesDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


JiraIssuesDataType.JIRA_ISSUES = JiraIssuesDataType("jira_issues")
