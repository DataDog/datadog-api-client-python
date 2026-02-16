"""
Pick relevant actions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.client_type import ClientType
from datadog_api_client.v2.model.pick_action_request import PickActionRequest
from datadog_api_client.v2.model.stability_level import StabilityLevel

body = PickActionRequest(
    client=ClientType.WORKFLOWS,
    number_of_relevant_actions=5,
    stability=StabilityLevel.STABLE,
    user_prompt="Send a Slack message",
)

configuration = Configuration()
configuration.unstable_operations["create_pick_action"] = True
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.create_pick_action(body=body)

    print(response)
