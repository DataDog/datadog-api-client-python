"""
Delete LLM Observability experiments returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_delete_experiments_data_attributes_request import (
    LLMObsDeleteExperimentsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_delete_experiments_data_request import LLMObsDeleteExperimentsDataRequest
from datadog_api_client.v2.model.llm_obs_delete_experiments_request import LLMObsDeleteExperimentsRequest
from datadog_api_client.v2.model.llm_obs_experiment_type import LLMObsExperimentType

body = LLMObsDeleteExperimentsRequest(
    data=LLMObsDeleteExperimentsDataRequest(
        attributes=LLMObsDeleteExperimentsDataAttributesRequest(
            experiment_ids=[
                "3fd6b5e0-8910-4b1c-a7d0-5b84de329012",
            ],
        ),
        type=LLMObsExperimentType.EXPERIMENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_experiments"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    api_instance.delete_llm_obs_experiments(body=body)
