"""
Generate data transformation code returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.chat_history_item import ChatHistoryItem
from datadog_api_client.v2.model.chat_history_item_role import ChatHistoryItemRole
from datadog_api_client.v2.model.data_transformation_context import DataTransformationContext
from datadog_api_client.v2.model.data_transformation_language import DataTransformationLanguage
from datadog_api_client.v2.model.data_transformation_request import DataTransformationRequest

body = DataTransformationRequest(
    chat_history=[
        ChatHistoryItem(
            content="Please add error handling",
            role=ChatHistoryItemRole.USER,
        ),
    ],
    context=DataTransformationContext(
        context_variables='{ "timestamp": 1234567890 }',
        current_script="return data.timestamp;",
    ),
    language=DataTransformationLanguage.JAVASCRIPT,
    stream=True,
    user_prompt="Convert timestamp to ISO format",
)

configuration = Configuration()
configuration.unstable_operations["create_data_transformation"] = True
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.create_data_transformation(body=body)
