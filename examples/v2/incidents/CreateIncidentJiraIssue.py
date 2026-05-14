"""
Create an incident Jira issue returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_jira_issue_data_attributes_request import (
    IncidentJiraIssueDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_jira_issue_data_request import IncidentJiraIssueDataRequest
from datadog_api_client.v2.model.incident_jira_issue_request import IncidentJiraIssueRequest
from datadog_api_client.v2.model.incident_jira_issue_type import IncidentJiraIssueType
from uuid import UUID

body = IncidentJiraIssueRequest(
    data=IncidentJiraIssueDataRequest(
        attributes=IncidentJiraIssueDataAttributesRequest(
            account_id="123456",
            issue_type_id="10001",
            project_id="10000",
            template_id=UUID("00000000-0000-0000-0000-000000000000"),
        ),
        type=IncidentJiraIssueType.INCIDENT_JIRA_ISSUES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_jira_issue"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_jira_issue(incident_id="incident_id", body=body)

    print(response)
