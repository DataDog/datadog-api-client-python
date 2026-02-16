"""
Create a custom agent conversation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.custom_agent_conversation_request import CustomAgentConversationRequest
from uuid import UUID

body = CustomAgentConversationRequest(
    conversation_id="550e8400-e29b-41d4-a716-446655440000",
    user_prompt="What is the weather like today?",
)

configuration = Configuration()
configuration.unstable_operations["create_custom_agent_conversation"] = True
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.create_custom_agent_conversation(
        custom_agent_id=UUID("3b796bda-b79b-477e-ae29-958473a683db"), body=body
    )
