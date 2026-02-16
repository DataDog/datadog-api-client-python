"""
Generate workflow scaffold with agentic stream returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.chat_message import ChatMessage
from datadog_api_client.v2.model.chat_message_role import ChatMessageRole
from datadog_api_client.v2.model.user_context import UserContext
from datadog_api_client.v2.model.user_info import UserInfo
from datadog_api_client.v2.model.workflow_scaffold_agentic_stream_request import WorkflowScaffoldAgenticStreamRequest

body = WorkflowScaffoldAgenticStreamRequest(
    chat_history=[
        ChatMessage(
            chat_id="chat-456",
            content="Add error handling to the workflow",
            id="msg-123",
            role=ChatMessageRole.USER,
            user_uuid="550e8400-e29b-41d4-a716-446655440000",
        ),
    ],
    previous_action="created_initial_scaffold",
    user_context=UserContext(
        user_info=UserInfo(
            org_name="Acme Corp",
            user_email="john.doe@example.com",
            user_name="John Doe",
            user_uuid="550e8400-e29b-41d4-a716-446655440000",
        ),
    ),
    user_prompt="Create a workflow to restart a service when CPU is high",
)

configuration = Configuration()
configuration.unstable_operations["create_workflow_scaffold_agentic_stream"] = True
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.create_workflow_scaffold_agentic_stream(body=body)
