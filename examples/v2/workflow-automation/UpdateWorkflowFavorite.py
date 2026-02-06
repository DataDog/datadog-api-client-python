"""
Update workflow favorite status returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.workflow_favorite_request import WorkflowFavoriteRequest
from datadog_api_client.v2.model.workflow_favorite_request_attributes import WorkflowFavoriteRequestAttributes
from datadog_api_client.v2.model.workflow_favorite_request_data import WorkflowFavoriteRequestData
from datadog_api_client.v2.model.workflow_favorite_request_type import WorkflowFavoriteRequestType

body = WorkflowFavoriteRequest(
    data=WorkflowFavoriteRequestData(
        attributes=WorkflowFavoriteRequestAttributes(
            favorite=True,
        ),
        type=WorkflowFavoriteRequestType.WORKFLOW_FAVORITE_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_workflow_favorite"] = True
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    api_instance.update_workflow_favorite(workflow_id="workflow_id", body=body)
