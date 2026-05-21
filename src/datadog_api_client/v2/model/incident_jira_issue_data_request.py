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
    from datadog_api_client.v2.model.incident_jira_issue_data_attributes_request import (
        IncidentJiraIssueDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_jira_issue_type import IncidentJiraIssueType


class IncidentJiraIssueDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_jira_issue_data_attributes_request import (
            IncidentJiraIssueDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_jira_issue_type import IncidentJiraIssueType

        return {
            "attributes": (IncidentJiraIssueDataAttributesRequest,),
            "type": (IncidentJiraIssueType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: IncidentJiraIssueDataAttributesRequest, type: IncidentJiraIssueType, **kwargs):
        """
        Jira issue data for a request.

        :param attributes: Attributes for creating a Jira issue from an incident.
        :type attributes: IncidentJiraIssueDataAttributesRequest

        :param type: Incident Jira issue resource type.
        :type type: IncidentJiraIssueType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
