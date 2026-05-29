"""
Clone an LLM Observability dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_dataset_clone_data_attributes_request import (
    LLMObsDatasetCloneDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_dataset_clone_data_request import LLMObsDatasetCloneDataRequest
from datadog_api_client.v2.model.llm_obs_dataset_clone_request import LLMObsDatasetCloneRequest
from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType

body = LLMObsDatasetCloneRequest(
    data=LLMObsDatasetCloneDataRequest(
        attributes=LLMObsDatasetCloneDataAttributesRequest(
            description="Clone of the original dataset for experimentation.",
            name="My cloned dataset",
        ),
        id="9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d",
        type=LLMObsDatasetType.DATASETS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["clone_llm_obs_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.clone_llm_obs_dataset(project_id="project_id", dataset_id="dataset_id", body=body)

    print(response)
