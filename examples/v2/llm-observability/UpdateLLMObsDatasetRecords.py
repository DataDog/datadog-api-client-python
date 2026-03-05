"""
Update LLM Observability dataset records returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_dataset_record_update_item import LLMObsDatasetRecordUpdateItem
from datadog_api_client.v2.model.llm_obs_dataset_records_update_data_attributes_request import (
    LLMObsDatasetRecordsUpdateDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_dataset_records_update_data_request import (
    LLMObsDatasetRecordsUpdateDataRequest,
)
from datadog_api_client.v2.model.llm_obs_dataset_records_update_request import LLMObsDatasetRecordsUpdateRequest
from datadog_api_client.v2.model.llm_obs_record_type import LLMObsRecordType

body = LLMObsDatasetRecordsUpdateRequest(
    data=LLMObsDatasetRecordsUpdateDataRequest(
        attributes=LLMObsDatasetRecordsUpdateDataAttributesRequest(
            records=[
                LLMObsDatasetRecordUpdateItem(
                    expected_output=None,
                    id="rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c",
                    input=None,
                ),
            ],
        ),
        type=LLMObsRecordType.RECORDS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_llm_obs_dataset_records"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.update_llm_obs_dataset_records(project_id="project_id", dataset_id="dataset_id", body=body)

    print(response)
