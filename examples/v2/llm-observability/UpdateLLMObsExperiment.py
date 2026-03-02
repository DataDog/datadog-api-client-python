"""
Update an LLM Observability experiment returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_experiment_type import LLMObsExperimentType
from datadog_api_client.v2.model.llm_obs_experiment_update_data_attributes_request import (
    LLMObsExperimentUpdateDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_experiment_update_data_request import LLMObsExperimentUpdateDataRequest
from datadog_api_client.v2.model.llm_obs_experiment_update_request import LLMObsExperimentUpdateRequest

body = LLMObsExperimentUpdateRequest(
    data=LLMObsExperimentUpdateDataRequest(
        attributes=LLMObsExperimentUpdateDataAttributesRequest(),
        type=LLMObsExperimentType.EXPERIMENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_llm_obs_experiment"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.update_llm_obs_experiment(experiment_id="experiment_id", body=body)

    print(response)
