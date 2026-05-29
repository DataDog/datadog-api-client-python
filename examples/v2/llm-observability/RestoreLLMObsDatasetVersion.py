"""
Restore an LLM Observability dataset version returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_dataset_restore_version_data_attributes_request import (
    LLMObsDatasetRestoreVersionDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_dataset_restore_version_data_request import (
    LLMObsDatasetRestoreVersionDataRequest,
)
from datadog_api_client.v2.model.llm_obs_dataset_restore_version_request import LLMObsDatasetRestoreVersionRequest
from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType

body = LLMObsDatasetRestoreVersionRequest(
    data=LLMObsDatasetRestoreVersionDataRequest(
        attributes=LLMObsDatasetRestoreVersionDataAttributesRequest(
            dataset_version=1,
        ),
        id="9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d",
        type=LLMObsDatasetType.DATASETS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["restore_llm_obs_dataset_version"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    api_instance.restore_llm_obs_dataset_version(project_id="project_id", dataset_id="dataset_id", body=body)
