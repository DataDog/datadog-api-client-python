"""
Execute a workflow returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.workflow_instance_create_meta import WorkflowInstanceCreateMeta
from datadog_api_client.v2.model.workflow_instance_create_request import WorkflowInstanceCreateRequest

body = WorkflowInstanceCreateRequest(
    meta=WorkflowInstanceCreateMeta(
        payload=dict([("input", "value")]),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.create_workflow_instance(workflow_id="ccf73164-1998-4785-a7a3-8d06c7e5f558", body=body)

    print(response)
