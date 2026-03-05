"""
Delete LLM Observability projects returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_delete_projects_data_attributes_request import (
    LLMObsDeleteProjectsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_delete_projects_data_request import LLMObsDeleteProjectsDataRequest
from datadog_api_client.v2.model.llm_obs_delete_projects_request import LLMObsDeleteProjectsRequest
from datadog_api_client.v2.model.llm_obs_project_type import LLMObsProjectType

body = LLMObsDeleteProjectsRequest(
    data=LLMObsDeleteProjectsDataRequest(
        attributes=LLMObsDeleteProjectsDataAttributesRequest(
            project_ids=[
                "a33671aa-24fd-4dcd-9b33-a8ec7dde7751",
            ],
        ),
        type=LLMObsProjectType.PROJECTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_projects"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    api_instance.delete_llm_obs_projects(body=body)
