"""
Update an AI workflow returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dependency_management_api import DependencyManagementApi
from datadog_api_client.v2.model.entity import Entity
from datadog_api_client.v2.model.filtering_logic import FilteringLogic
from datadog_api_client.v2.model.update_ai_workflow_request import UpdateAIWorkflowRequest
from datetime import datetime
from dateutil.tz import tzutc
from uuid import UUID

body = UpdateAIWorkflowRequest(
    completed_at=datetime(2024, 6, 1, 12, 0, tzinfo=tzutc()),
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
    grouping_logic="by-team",
    max_number_of_entities_per_session=10,
    prompt="Updated prompt for the dependency upgrade",
    repository="DataDog/datadog-agent",
    workflow_name="Updated workflow name",
)

configuration = Configuration()
configuration.unstable_operations["update_ai_workflow"] = True
with ApiClient(configuration) as api_client:
    api_instance = DependencyManagementApi(api_client)
    response = api_instance.update_ai_workflow(id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
