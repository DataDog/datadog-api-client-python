"""
Link existing Jira issue to case returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.jira_issue_link_attributes import JiraIssueLinkAttributes
from datadog_api_client.v2.model.jira_issue_link_data import JiraIssueLinkData
from datadog_api_client.v2.model.jira_issue_link_request import JiraIssueLinkRequest
from datadog_api_client.v2.model.jira_issue_resource_type import JiraIssueResourceType

body = JiraIssueLinkRequest(
    data=JiraIssueLinkData(
        attributes=JiraIssueLinkAttributes(
            jira_issue_url="https://jira.example.com/browse/PROJ-123",
        ),
        type=JiraIssueResourceType.ISSUES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["link_jira_issue_to_case"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.link_jira_issue_to_case(case_id="case_id", body=body)
