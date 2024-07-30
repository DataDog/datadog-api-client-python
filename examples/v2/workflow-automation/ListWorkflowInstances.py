"""
List workflow instances returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.list_workflow_instances(
        workflow_id="ccf73164-1998-4785-a7a3-8d06c7e5f558",
    )

    print(response)
