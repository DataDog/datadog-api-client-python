# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentJiraIssueType(ModelSimple):
    """
    Incident Jira issue resource type.

    :param value: If omitted defaults to "incident_jira_issues". Must be one of ["incident_jira_issues"].
    :type value: str
    """

    allowed_values = {
        "incident_jira_issues",
    }
    INCIDENT_JIRA_ISSUES: ClassVar["IncidentJiraIssueType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentJiraIssueType.INCIDENT_JIRA_ISSUES = IncidentJiraIssueType("incident_jira_issues")
