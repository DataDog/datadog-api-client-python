"""
Update an LLM Observability dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType
from datadog_api_client.v2.model.llm_obs_dataset_update_data_attributes_request import (
    LLMObsDatasetUpdateDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_dataset_update_data_request import LLMObsDatasetUpdateDataRequest
from datadog_api_client.v2.model.llm_obs_dataset_update_request import LLMObsDatasetUpdateRequest

body = LLMObsDatasetUpdateRequest(
    data=LLMObsDatasetUpdateDataRequest(
        attributes=LLMObsDatasetUpdateDataAttributesRequest(),
        type=LLMObsDatasetType.DATASETS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_llm_obs_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.update_llm_obs_dataset(project_id="project_id", dataset_id="dataset_id", body=body)

    print(response)
