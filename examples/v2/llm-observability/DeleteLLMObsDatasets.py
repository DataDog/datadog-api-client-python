"""
Delete LLM Observability datasets returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType
from datadog_api_client.v2.model.llm_obs_delete_datasets_data_attributes_request import (
    LLMObsDeleteDatasetsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_delete_datasets_data_request import LLMObsDeleteDatasetsDataRequest
from datadog_api_client.v2.model.llm_obs_delete_datasets_request import LLMObsDeleteDatasetsRequest

body = LLMObsDeleteDatasetsRequest(
    data=LLMObsDeleteDatasetsDataRequest(
        attributes=LLMObsDeleteDatasetsDataAttributesRequest(
            dataset_ids=[
                "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d",
            ],
        ),
        type=LLMObsDatasetType.DATASETS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_datasets"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    api_instance.delete_llm_obs_datasets(project_id="project_id", body=body)
