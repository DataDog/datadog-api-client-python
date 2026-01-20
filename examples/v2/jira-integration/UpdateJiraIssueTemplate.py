"""
Update Jira issue template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi
from datadog_api_client.v2.model.jira_issue_template_type import JiraIssueTemplateType
from datadog_api_client.v2.model.jira_issue_template_update_request import JiraIssueTemplateUpdateRequest
from datadog_api_client.v2.model.jira_issue_template_update_request_attributes import (
    JiraIssueTemplateUpdateRequestAttributes,
)
from datadog_api_client.v2.model.jira_issue_template_update_request_data import JiraIssueTemplateUpdateRequestData
from uuid import UUID

body = JiraIssueTemplateUpdateRequest(
    data=JiraIssueTemplateUpdateRequestData(
        attributes=JiraIssueTemplateUpdateRequestAttributes(
            fields=dict([("description", "{'payload': 'Updated Description', 'type': 'json'}")]),
            name="test_template_updated",
        ),
        type=JiraIssueTemplateType.JIRA_ISSUE_TEMPLATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_jira_issue_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    response = api_instance.update_jira_issue_template(
        issue_template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
