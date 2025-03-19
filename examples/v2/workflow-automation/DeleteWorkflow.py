"""
Delete an existing Workflow returns "Successfully deleted a workflow." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi

# there is a valid "workflow" in the system
WORKFLOW_DATA_ID = environ["WORKFLOW_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    api_instance.delete_workflow(
        workflow_id=WORKFLOW_DATA_ID,
    )
