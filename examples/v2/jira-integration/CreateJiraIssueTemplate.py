"""
Create Jira issue template returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi
from datadog_api_client.v2.model.jira_issue_template_create_request import JiraIssueTemplateCreateRequest
from datadog_api_client.v2.model.jira_issue_template_create_request_attributes import (
    JiraIssueTemplateCreateRequestAttributes,
)
from datadog_api_client.v2.model.jira_issue_template_create_request_attributes_jira_account import (
    JiraIssueTemplateCreateRequestAttributesJiraAccount,
)
from datadog_api_client.v2.model.jira_issue_template_create_request_data import JiraIssueTemplateCreateRequestData
from datadog_api_client.v2.model.jira_issue_template_type import JiraIssueTemplateType
from uuid import UUID

body = JiraIssueTemplateCreateRequest(
    data=JiraIssueTemplateCreateRequestData(
        attributes=JiraIssueTemplateCreateRequestAttributes(
            fields=dict([("description", "{'payload': 'Test', 'type': 'json'}")]),
            issue_type_id="12730",
            jira_account=JiraIssueTemplateCreateRequestAttributesJiraAccount(
                id=UUID("80f16d40-1fba-486e-b1fc-983e6ca19bec"),
            ),
            name="test-template",
            project_id="10772",
        ),
        type=JiraIssueTemplateType.JIRA_ISSUE_TEMPLATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_jira_issue_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    response = api_instance.create_jira_issue_template(body=body)

    print(response)
