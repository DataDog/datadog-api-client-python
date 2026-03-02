"""
Create an LLM Observability dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_dataset_data_attributes_request import LLMObsDatasetDataAttributesRequest
from datadog_api_client.v2.model.llm_obs_dataset_data_request import LLMObsDatasetDataRequest
from datadog_api_client.v2.model.llm_obs_dataset_request import LLMObsDatasetRequest
from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType

body = LLMObsDatasetRequest(
    data=LLMObsDatasetDataRequest(
        attributes=LLMObsDatasetDataAttributesRequest(
            name="My LLM Dataset",
        ),
        type=LLMObsDatasetType.DATASETS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.create_llm_obs_dataset(project_id="project_id", body=body)

    print(response)
