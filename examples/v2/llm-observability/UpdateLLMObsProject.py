"""
Update an LLM Observability project returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_project_type import LLMObsProjectType
from datadog_api_client.v2.model.llm_obs_project_update_data_attributes_request import (
    LLMObsProjectUpdateDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_project_update_data_request import LLMObsProjectUpdateDataRequest
from datadog_api_client.v2.model.llm_obs_project_update_request import LLMObsProjectUpdateRequest

body = LLMObsProjectUpdateRequest(
    data=LLMObsProjectUpdateDataRequest(
        attributes=LLMObsProjectUpdateDataAttributesRequest(),
        type=LLMObsProjectType.PROJECTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_llm_obs_project"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.update_llm_obs_project(project_id="project_id", body=body)

    print(response)
