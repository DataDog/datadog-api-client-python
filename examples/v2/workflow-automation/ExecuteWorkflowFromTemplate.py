"""
Execute a workflow from a template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.workflow_headless_execution_config import WorkflowHeadlessExecutionConfig
from datadog_api_client.v2.model.workflow_headless_execution_connection import WorkflowHeadlessExecutionConnection
from datadog_api_client.v2.model.workflow_headless_execution_request import WorkflowHeadlessExecutionRequest
from datadog_api_client.v2.model.workflow_headless_execution_request_attributes import (
    WorkflowHeadlessExecutionRequestAttributes,
)
from datadog_api_client.v2.model.workflow_headless_execution_request_data import WorkflowHeadlessExecutionRequestData
from datadog_api_client.v2.model.workflow_headless_execution_request_type import WorkflowHeadlessExecutionRequestType
from uuid import UUID

body = WorkflowHeadlessExecutionRequest(
    data=WorkflowHeadlessExecutionRequestData(
        attributes=WorkflowHeadlessExecutionRequestAttributes(
            config=WorkflowHeadlessExecutionConfig(
                connections=[
                    WorkflowHeadlessExecutionConnection(
                        connection_id=UUID("11111111-1111-1111-1111-111111111111"),
                        label="INTEGRATION_DATADOG",
                    ),
                ],
                inputs=dict(),
            ),
            template_id="template-789",
        ),
        id="1234",
        type=WorkflowHeadlessExecutionRequestType.WORKFLOW_HEADLESS_EXECUTION_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["execute_workflow_from_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.execute_workflow_from_template(parent_id="parent_id", body=body)

    print(response)
