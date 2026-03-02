"""
Create an LLM Observability experiment returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_experiment_data_attributes_request import LLMObsExperimentDataAttributesRequest
from datadog_api_client.v2.model.llm_obs_experiment_data_request import LLMObsExperimentDataRequest
from datadog_api_client.v2.model.llm_obs_experiment_request import LLMObsExperimentRequest
from datadog_api_client.v2.model.llm_obs_experiment_type import LLMObsExperimentType

body = LLMObsExperimentRequest(
    data=LLMObsExperimentDataRequest(
        attributes=LLMObsExperimentDataAttributesRequest(
            dataset_id="9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d",
            name="My Experiment v1",
            project_id="a33671aa-24fd-4dcd-9b33-a8ec7dde7751",
        ),
        type=LLMObsExperimentType.EXPERIMENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_experiment"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.create_llm_obs_experiment(body=body)

    print(response)
