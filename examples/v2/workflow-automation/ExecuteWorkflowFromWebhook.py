"""
Execute a workflow from a webhook returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.workflow_webhook_payload import WorkflowWebhookPayload
from uuid import UUID

body = WorkflowWebhookPayload([("foo", "bar")])

configuration = Configuration()
configuration.unstable_operations["execute_workflow_from_webhook"] = True
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.execute_workflow_from_webhook(
        workflow_id="workflow_id",
        org_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        x_hub_signature_256="sha256=abcdef123456...",
        user_agent="GitHub-Hookshot/abc123",
        body=body,
    )

    print(response)
