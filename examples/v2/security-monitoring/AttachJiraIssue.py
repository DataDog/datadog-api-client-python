"""
Attach security findings to a Jira issue returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.attach_jira_issue_request import AttachJiraIssueRequest
from datadog_api_client.v2.model.attach_jira_issue_request_data import AttachJiraIssueRequestData
from datadog_api_client.v2.model.attach_jira_issue_request_data_attributes import AttachJiraIssueRequestDataAttributes
from datadog_api_client.v2.model.attach_jira_issue_request_data_relationships import (
    AttachJiraIssueRequestDataRelationships,
)
from datadog_api_client.v2.model.case_management_project import CaseManagementProject
from datadog_api_client.v2.model.case_management_project_data import CaseManagementProjectData
from datadog_api_client.v2.model.case_management_project_data_type import CaseManagementProjectDataType
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings
from datadog_api_client.v2.model.jira_issues_data_type import JiraIssuesDataType

body = AttachJiraIssueRequest(
    data=AttachJiraIssueRequestData(
        attributes=AttachJiraIssueRequestDataAttributes(
            jira_issue_url="https://datadoghq-sandbox-538.atlassian.net/browse/CSMSEC-105476",
        ),
        relationships=AttachJiraIssueRequestDataRelationships(
            findings=Findings(
                data=[
                    FindingData(
                        id="OTQ3NjJkMmYwMTIzMzMxNTc1Y2Q4MTA5NWU0NTBmMDl-ZjE3NjMxZWVkYzBjZGI1NDY2NWY2OGQxZDk4MDY4MmI=",
                        type=FindingDataType.FINDINGS,
                    ),
                    FindingData(
                        id="MTNjN2ZmYWMzMDIxYmU1ZDFiZDRjNWUwN2I1NzVmY2F-YTA3MzllMTUzNWM3NmEyZjdiNzEzOWM5YmViZTMzOGM=",
                        type=FindingDataType.FINDINGS,
                    ),
                ],
            ),
            project=CaseManagementProject(
                data=CaseManagementProjectData(
                    id="959a6f71-bac8-4027-b1d3-2264f569296f",
                    type=CaseManagementProjectDataType.PROJECTS,
                ),
            ),
        ),
        type=JiraIssuesDataType.JIRA_ISSUES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.attach_jira_issue(body=body)

    print(response)
