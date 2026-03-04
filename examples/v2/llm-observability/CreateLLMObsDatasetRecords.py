"""
Append records to an LLM Observability dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_dataset_record_item import LLMObsDatasetRecordItem
from datadog_api_client.v2.model.llm_obs_dataset_records_data_attributes_request import (
    LLMObsDatasetRecordsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_dataset_records_data_request import LLMObsDatasetRecordsDataRequest
from datadog_api_client.v2.model.llm_obs_dataset_records_request import LLMObsDatasetRecordsRequest
from datadog_api_client.v2.model.llm_obs_record_type import LLMObsRecordType

body = LLMObsDatasetRecordsRequest(
    data=LLMObsDatasetRecordsDataRequest(
        attributes=LLMObsDatasetRecordsDataAttributesRequest(
            records=[
                LLMObsDatasetRecordItem(
                    expected_output=None,
                    input=None,
                ),
            ],
        ),
        type=LLMObsRecordType.RECORDS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_dataset_records"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.create_llm_obs_dataset_records(project_id="project_id", dataset_id="dataset_id", body=body)

    print(response)
