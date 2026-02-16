"""
Create Jira issues for security findings returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.finding_status import FindingStatus
from datadog_api_client.v2.model.jira_issue_custom_fields import JiraIssueCustomFields
from datadog_api_client.v2.model.jira_issue_data_attributes_request import JiraIssueDataAttributesRequest
from datadog_api_client.v2.model.jira_issue_data_attributes_request_mode import JiraIssueDataAttributesRequestMode
from datadog_api_client.v2.model.jira_issue_data_meta import JiraIssueDataMeta
from datadog_api_client.v2.model.jira_issue_data_request import JiraIssueDataRequest
from datadog_api_client.v2.model.jira_issue_finding import JiraIssueFinding
from datadog_api_client.v2.model.jira_issue_finding_id import JiraIssueFindingId
from datadog_api_client.v2.model.jira_issue_request import JiraIssueRequest
from datadog_api_client.v2.model.jira_issue_type import JiraIssueType

body = JiraIssueRequest(
    data=JiraIssueDataRequest(
        attributes=JiraIssueDataAttributesRequest(
            account_id="f7ccdf99-0e22-4378-bdf9-03fde5379fea",
            fields=JiraIssueCustomFields([("customfield_10000", "Custom field value")]),
            issue_type="story",
            issuetype_id="1235",
            mode=JiraIssueDataAttributesRequestMode.SINGLE,
            project_id="1234",
            project_key="SEC",
        ),
        id="ID",
        meta=JiraIssueDataMeta(
            findings=[
                JiraIssueFinding(
                    description="Description",
                    ids=[
                        JiraIssueFindingId(
                            discovered=123213123,
                            id="afa-afa-hze",
                            resource="Resource",
                            tags="akjasd:asdsad",
                        ),
                    ],
                    impacted=1,
                    references="",
                    remediation="Remediation",
                    severity=FindingStatus.CRITICAL,
                    title="Title",
                    type="ciem",
                ),
            ],
            vulnerabilities=[
                JiraIssueFinding(
                    description="Description",
                    ids=[
                        JiraIssueFindingId(
                            discovered=123213123,
                            id="afa-afa-hze",
                            resource="Resource",
                            tags="akjasd:asdsad",
                        ),
                    ],
                    impacted=1,
                    references="",
                    remediation="Remediation",
                    severity=FindingStatus.CRITICAL,
                    title="Title",
                    type="ciem",
                ),
            ],
        ),
        type=JiraIssueType.JIRA_ISSUE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_jira_issue"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.create_jira_issue(body=body)
