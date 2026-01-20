"""
Delete Jira account returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_jira_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    api_instance.delete_jira_account(
        account_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )
