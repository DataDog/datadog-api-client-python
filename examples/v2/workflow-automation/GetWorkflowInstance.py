"""
Get a workflow instance returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.get_workflow_instance(
        workflow_id="ccf73164-1998-4785-a7a3-8d06c7e5f558",
        instance_id="305a472b-71ab-4ce8-8f8d-75db635627b5",
    )

    print(response)
