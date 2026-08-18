"""
Delete LLM Observability data returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_data_deletion_request import LLMObsDataDeletionRequest
from datadog_api_client.v2.model.llm_obs_data_deletion_request_attributes import LLMObsDataDeletionRequestAttributes
from datadog_api_client.v2.model.llm_obs_data_deletion_request_data import LLMObsDataDeletionRequestData
from datadog_api_client.v2.model.llm_obs_data_deletion_request_type import LLMObsDataDeletionRequestType

body = LLMObsDataDeletionRequest(
    data=LLMObsDataDeletionRequestData(
        attributes=LLMObsDataDeletionRequestAttributes(
            delay=0,
            _from=1705314600000,
            query=dict(
                query="@trace_id:abc123def456",
            ),
            to=1705315200000,
        ),
        type=LLMObsDataDeletionRequestType.CREATE_DELETION_REQ,
    ),
)

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_data"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.delete_llm_obs_data(body=body)

    print(response)
