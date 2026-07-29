# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentRuleTaskIDType(ModelSimple):
    """
    The task ID for an incident rule.

    :param value: Must be one of ["jira-create-issue-job", "notify-incident-handles-job", "servicenow-create-incident-job", "slack-create-channel-job", "zoom-create-meeting-job", "google-meet-create-meeting-job", "workflow-automation-job", "ms-teams-create-meeting-job", "google-chat-create-space-job", "zoom-suppress-summarization-job", "ms-teams-suppress-summarization-job", "google-meet-suppress-summarization-job"].
    :type value: str
    """

    allowed_values = {
        "jira-create-issue-job",
        "notify-incident-handles-job",
        "servicenow-create-incident-job",
        "slack-create-channel-job",
        "zoom-create-meeting-job",
        "google-meet-create-meeting-job",
        "workflow-automation-job",
        "ms-teams-create-meeting-job",
        "google-chat-create-space-job",
        "zoom-suppress-summarization-job",
        "ms-teams-suppress-summarization-job",
        "google-meet-suppress-summarization-job",
    }
    JIRA_CREATE_ISSUE_JOB: ClassVar["IncidentRuleTaskIDType"]
    NOTIFY_INCIDENT_HANDLES_JOB: ClassVar["IncidentRuleTaskIDType"]
    SERVICENOW_CREATE_INCIDENT_JOB: ClassVar["IncidentRuleTaskIDType"]
    SLACK_CREATE_CHANNEL_JOB: ClassVar["IncidentRuleTaskIDType"]
    ZOOM_CREATE_MEETING_JOB: ClassVar["IncidentRuleTaskIDType"]
    GOOGLE_MEET_CREATE_MEETING_JOB: ClassVar["IncidentRuleTaskIDType"]
    WORKFLOW_AUTOMATION_JOB: ClassVar["IncidentRuleTaskIDType"]
    MS_TEAMS_CREATE_MEETING_JOB: ClassVar["IncidentRuleTaskIDType"]
    GOOGLE_CHAT_CREATE_SPACE_JOB: ClassVar["IncidentRuleTaskIDType"]
    ZOOM_SUPPRESS_SUMMARIZATION_JOB: ClassVar["IncidentRuleTaskIDType"]
    MS_TEAMS_SUPPRESS_SUMMARIZATION_JOB: ClassVar["IncidentRuleTaskIDType"]
    GOOGLE_MEET_SUPPRESS_SUMMARIZATION_JOB: ClassVar["IncidentRuleTaskIDType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentRuleTaskIDType.JIRA_CREATE_ISSUE_JOB = IncidentRuleTaskIDType("jira-create-issue-job")
IncidentRuleTaskIDType.NOTIFY_INCIDENT_HANDLES_JOB = IncidentRuleTaskIDType("notify-incident-handles-job")
IncidentRuleTaskIDType.SERVICENOW_CREATE_INCIDENT_JOB = IncidentRuleTaskIDType("servicenow-create-incident-job")
IncidentRuleTaskIDType.SLACK_CREATE_CHANNEL_JOB = IncidentRuleTaskIDType("slack-create-channel-job")
IncidentRuleTaskIDType.ZOOM_CREATE_MEETING_JOB = IncidentRuleTaskIDType("zoom-create-meeting-job")
IncidentRuleTaskIDType.GOOGLE_MEET_CREATE_MEETING_JOB = IncidentRuleTaskIDType("google-meet-create-meeting-job")
IncidentRuleTaskIDType.WORKFLOW_AUTOMATION_JOB = IncidentRuleTaskIDType("workflow-automation-job")
IncidentRuleTaskIDType.MS_TEAMS_CREATE_MEETING_JOB = IncidentRuleTaskIDType("ms-teams-create-meeting-job")
IncidentRuleTaskIDType.GOOGLE_CHAT_CREATE_SPACE_JOB = IncidentRuleTaskIDType("google-chat-create-space-job")
IncidentRuleTaskIDType.ZOOM_SUPPRESS_SUMMARIZATION_JOB = IncidentRuleTaskIDType("zoom-suppress-summarization-job")
IncidentRuleTaskIDType.MS_TEAMS_SUPPRESS_SUMMARIZATION_JOB = IncidentRuleTaskIDType(
    "ms-teams-suppress-summarization-job"
)
IncidentRuleTaskIDType.GOOGLE_MEET_SUPPRESS_SUMMARIZATION_JOB = IncidentRuleTaskIDType(
    "google-meet-suppress-summarization-job"
)
