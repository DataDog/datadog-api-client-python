"""
Create an LLM Observability project returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_project_data_attributes_request import LLMObsProjectDataAttributesRequest
from datadog_api_client.v2.model.llm_obs_project_data_request import LLMObsProjectDataRequest
from datadog_api_client.v2.model.llm_obs_project_request import LLMObsProjectRequest
from datadog_api_client.v2.model.llm_obs_project_type import LLMObsProjectType

body = LLMObsProjectRequest(
    data=LLMObsProjectDataRequest(
        attributes=LLMObsProjectDataAttributesRequest(
            name="My LLM Project",
        ),
        type=LLMObsProjectType.PROJECTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_project"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.create_llm_obs_project(body=body)

    print(response)
