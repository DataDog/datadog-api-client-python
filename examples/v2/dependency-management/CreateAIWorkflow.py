"""
Create an AI workflow returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dependency_management_api import DependencyManagementApi
from datadog_api_client.v2.model.create_ai_workflow_request import CreateAIWorkflowRequest
from datadog_api_client.v2.model.entity import Entity
from datadog_api_client.v2.model.filtering_logic import FilteringLogic

body = CreateAIWorkflowRequest(
    entities=[
        [
            Entity(
                entity_kind="service",
                entity_name="my-service",
                entity_namespace="default",
                entity_team="platform",
            ),
        ],
    ],
    filtering_logic=FilteringLogic([("teams", "['platform']")]),
    grouping_logic="by-service",
    idp_campaign_id="campaign-abc123",
    max_number_of_entities_per_session=5,
    prompt="Upgrade the lodash dependency to version 4.17.21",
    repository="DataDog/datadog-agent",
    user="john.doe@example.com",
    workflow_name="Upgrade lodash to 4.17.21",
)

configuration = Configuration()
configuration.unstable_operations["create_ai_workflow"] = True
with ApiClient(configuration) as api_client:
    api_instance = DependencyManagementApi(api_client)
    response = api_instance.create_ai_workflow(body=body)

    print(response)
