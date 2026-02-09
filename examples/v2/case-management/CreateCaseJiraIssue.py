"""
Create Jira issue for case returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.jira_issue_create_attributes import JiraIssueCreateAttributes
from datadog_api_client.v2.model.jira_issue_create_data import JiraIssueCreateData
from datadog_api_client.v2.model.jira_issue_create_request import JiraIssueCreateRequest
from datadog_api_client.v2.model.jira_issue_resource_type import JiraIssueResourceType

body = JiraIssueCreateRequest(
    data=JiraIssueCreateData(
        attributes=JiraIssueCreateAttributes(
            fields=dict(),
            issue_type_id="10001",
            jira_account_id="1234",
            project_id="5678",
        ),
        type=JiraIssueResourceType.ISSUES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_case_jira_issue"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.create_case_jira_issue(case_id="case_id", body=body)
