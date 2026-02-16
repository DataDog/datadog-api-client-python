"""
Generate workflow description returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.workflow_description_request import WorkflowDescriptionRequest

body = WorkflowDescriptionRequest(
    name="Alert Response Workflow",
    spec=dict([("steps", "[{'actionId': 'com.datadoghq.slack.send_message', 'name': 'Send notification'}]")]),
)

configuration = Configuration()
configuration.unstable_operations["create_workflow_description"] = True
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.create_workflow_description(body=body)

    print(response)
