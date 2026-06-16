"""
List workflows returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    items = api_instance.list_workflows_with_pagination(
        limit=2,
        filter_query="Example-Workflow-Automation",
    )
    for item in items:
        print(item)
