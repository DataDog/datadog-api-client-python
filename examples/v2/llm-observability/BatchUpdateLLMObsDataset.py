"""
Batch update LLM Observability dataset records returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_dataset_batch_update_data_attributes_request import (
    LLMObsDatasetBatchUpdateDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_dataset_batch_update_data_request import LLMObsDatasetBatchUpdateDataRequest
from datadog_api_client.v2.model.llm_obs_dataset_batch_update_insert_record import LLMObsDatasetBatchUpdateInsertRecord
from datadog_api_client.v2.model.llm_obs_dataset_batch_update_request import LLMObsDatasetBatchUpdateRequest
from datadog_api_client.v2.model.llm_obs_dataset_batch_update_update_record import LLMObsDatasetBatchUpdateUpdateRecord
from datadog_api_client.v2.model.llm_obs_dataset_record_tag_operations import LLMObsDatasetRecordTagOperations
from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType

body = LLMObsDatasetBatchUpdateRequest(
    data=LLMObsDatasetBatchUpdateDataRequest(
        attributes=LLMObsDatasetBatchUpdateDataAttributesRequest(
            create_new_version=True,
            delete_records=[],
            insert_records=[
                LLMObsDatasetBatchUpdateInsertRecord(
                    expected_output=None,
                    id="rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c",
                    input=None,
                    tag_operations=LLMObsDatasetRecordTagOperations(
                        add=[],
                        remove=[],
                        set=[],
                    ),
                    tags=[],
                ),
            ],
            tags=[],
            update_records=[
                LLMObsDatasetBatchUpdateUpdateRecord(
                    expected_output=None,
                    id="rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c",
                    input=None,
                    tag_operations=LLMObsDatasetRecordTagOperations(
                        add=[],
                        remove=[],
                        set=[],
                    ),
                ),
            ],
        ),
        id="9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d",
        type=LLMObsDatasetType.DATASETS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["batch_update_llm_obs_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.batch_update_llm_obs_dataset(project_id="project_id", dataset_id="dataset_id", body=body)

    print(response)
