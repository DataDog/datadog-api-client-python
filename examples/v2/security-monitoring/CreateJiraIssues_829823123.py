"""
Create Jira issue for security findings returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.case_data_type import CaseDataType
from datadog_api_client.v2.model.case_management_project import CaseManagementProject
from datadog_api_client.v2.model.case_management_project_data import CaseManagementProjectData
from datadog_api_client.v2.model.case_management_project_data_type import CaseManagementProjectDataType
from datadog_api_client.v2.model.create_case_request_data import CreateCaseRequestData
from datadog_api_client.v2.model.create_case_request_data_attributes import CreateCaseRequestDataAttributes
from datadog_api_client.v2.model.create_case_request_data_relationships import CreateCaseRequestDataRelationships
from datadog_api_client.v2.model.create_jira_issue_request_array import CreateJiraIssueRequestArray
from datadog_api_client.v2.model.create_jira_issue_request_data import CreateJiraIssueRequestData
from datadog_api_client.v2.model.create_jira_issue_request_data_attributes import CreateJiraIssueRequestDataAttributes
from datadog_api_client.v2.model.create_jira_issue_request_data_relationships import (
    CreateJiraIssueRequestDataRelationships,
)
from datadog_api_client.v2.model.create_jira_issue_request_data_relationships_case import (
    CreateJiraIssueRequestDataRelationshipsCase,
)
from datadog_api_client.v2.model.create_jira_issue_request_data_relationships_case_data import (
    CreateJiraIssueRequestDataRelationshipsCaseData,
)
from datadog_api_client.v2.model.finding_data import FindingData
from datadog_api_client.v2.model.finding_data_type import FindingDataType
from datadog_api_client.v2.model.findings import Findings
from datadog_api_client.v2.model.jira_issues_data_type import JiraIssuesDataType

body = CreateJiraIssueRequestArray(
    data=[
        CreateJiraIssueRequestData(
            type=JiraIssuesDataType.JIRA_ISSUES,
            attributes=CreateJiraIssueRequestDataAttributes(),
            relationships=CreateJiraIssueRequestDataRelationships(
                case=CreateJiraIssueRequestDataRelationshipsCase(
                    data=CreateJiraIssueRequestDataRelationshipsCaseData(
                        type=CaseDataType.CASES,
                        id="e469ceda-957a-4557-a607-9ff25032e9ca",
                    ),
                ),
            ),
        ),
    ],
    included=[
        CreateCaseRequestData(
            type=CaseDataType.CASES,
            attributes=CreateCaseRequestDataAttributes(
                title="A title",
                description="A description",
            ),
            relationships=CreateCaseRequestDataRelationships(
                project=CaseManagementProject(
                    data=CaseManagementProjectData(
                        type=CaseManagementProjectDataType.PROJECTS,
                        id="959a6f71-bac8-4027-b1d3-2264f569296f",
                    ),
                ),
                findings=Findings(
                    data=[
                        FindingData(
                            type=FindingDataType.FINDINGS,
                            id="MzUxMDI4OWYyYWEyODRhYjQ0Zjg2YjY2ZTFmNjRjYzd-NDU2OWQyNTk1MjM5OGI2NzJjMTVhYjhiODY1ZDcwZWY=",
                        ),
                        FindingData(
                            type=FindingDataType.FINDINGS,
                            id="ZjE2ZGI5YjdmYTQyYzhhMDQ3Nzc3YjM1NGQ2Y2NmZTd-NDU2OWQyNTk1MjM5OGI2NzJjMTVhYjhiODY1ZDcwZWY=",
                        ),
                    ],
                ),
            ),
            id="e469ceda-957a-4557-a607-9ff25032e9ca",
        ),
        CaseManagementProjectData(
            type=CaseManagementProjectDataType.PROJECTS,
            id="959a6f71-bac8-4027-b1d3-2264f569296f",
        ),
        FindingData(
            type=FindingDataType.FINDINGS,
            id="MzUxMDI4OWYyYWEyODRhYjQ0Zjg2YjY2ZTFmNjRjYzd-NDU2OWQyNTk1MjM5OGI2NzJjMTVhYjhiODY1ZDcwZWY=",
        ),
        FindingData(
            type=FindingDataType.FINDINGS,
            id="ZjE2ZGI5YjdmYTQyYzhhMDQ3Nzc3YjM1NGQ2Y2NmZTd-NDU2OWQyNTk1MjM5OGI2NzJjMTVhYjhiODY1ZDcwZWY=",
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_jira_issues(body=body)

    print(response)
