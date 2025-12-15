"""
Create Jira issues for security findings returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.case_management_project import CaseManagementProject
from datadog_api_client.v2.model.case_management_project_data import CaseManagementProjectData
from datadog_api_client.v2.model.case_management_project_data_type import CaseManagementProjectDataType
from datadog_api_client.v2.model.case_priority import CasePriority
from datadog_api_client.v2.model.create_jira_issue_request_array import CreateJiraIssueRequestArray
from datadog_api_client.v2.model.create_jira_issue_request_data import CreateJiraIssueRequestData
from datadog_api_client.v2.model.create_jira_issue_request_data_attributes import CreateJiraIssueRequestDataAttributes
from datadog_api_client.v2.model.create_jira_issue_request_data_relationships import (
    CreateJiraIssueRequestDataRelationships,
)
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings
from datadog_api_client.v2.model.jira_issues_data_type import JiraIssuesDataType

body = CreateJiraIssueRequestArray(
    data=[
        CreateJiraIssueRequestData(
            attributes=CreateJiraIssueRequestDataAttributes(
                assignee_id="f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0",
                description="A description of the Jira issue.",
                fields=dict([("key1", "value"), ("key2", "['value']"), ("key3", "{'key4': 'value'}")]),
                priority=CasePriority.NOT_DEFINED,
                title="A title for the Jira issue.",
            ),
            relationships=CreateJiraIssueRequestDataRelationships(
                findings=Findings(
                    data=[
                        FindingData(
                            id="ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==",
                            type=FindingDataType.FINDINGS,
                        ),
                    ],
                ),
                project=CaseManagementProject(
                    data=CaseManagementProjectData(
                        id="aeadc05e-98a8-11ec-ac2c-da7ad0900001",
                        type=CaseManagementProjectDataType.PROJECTS,
                    ),
                ),
            ),
            type=JiraIssuesDataType.JIRA_ISSUES,
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["create_jira_issues"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_jira_issues(body=body)

    print(response)
