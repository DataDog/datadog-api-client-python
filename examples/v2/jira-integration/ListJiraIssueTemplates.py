"""
List Jira issue templates returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.jira_integration_api import JiraIntegrationApi

configuration = Configuration()
configuration.unstable_operations["list_jira_issue_templates"] = True
with ApiClient(configuration) as api_client:
    api_instance = JiraIntegrationApi(api_client)
    response = api_instance.list_jira_issue_templates()

    print(response)
