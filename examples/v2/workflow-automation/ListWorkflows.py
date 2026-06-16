"""
List workflows returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.list_workflows()

    print(response)
