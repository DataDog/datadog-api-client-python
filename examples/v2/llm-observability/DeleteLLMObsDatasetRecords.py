"""
Delete LLM Observability dataset records returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_delete_dataset_records_data_attributes_request import (
    LLMObsDeleteDatasetRecordsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_delete_dataset_records_data_request import (
    LLMObsDeleteDatasetRecordsDataRequest,
)
from datadog_api_client.v2.model.llm_obs_delete_dataset_records_request import LLMObsDeleteDatasetRecordsRequest
from datadog_api_client.v2.model.llm_obs_record_type import LLMObsRecordType

body = LLMObsDeleteDatasetRecordsRequest(
    data=LLMObsDeleteDatasetRecordsDataRequest(
        attributes=LLMObsDeleteDatasetRecordsDataAttributesRequest(
            record_ids=[
                "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c",
            ],
        ),
        type=LLMObsRecordType.RECORDS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_dataset_records"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    api_instance.delete_llm_obs_dataset_records(project_id="project_id", dataset_id="dataset_id", body=body)
