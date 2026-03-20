"""
Trigger a deployment gates evaluation returns "Accepted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from datadog_api_client.v2.model.deployment_gates_evaluation_request import DeploymentGatesEvaluationRequest
from datadog_api_client.v2.model.deployment_gates_evaluation_request_attributes import (
    DeploymentGatesEvaluationRequestAttributes,
)
from datadog_api_client.v2.model.deployment_gates_evaluation_request_data import DeploymentGatesEvaluationRequestData
from datadog_api_client.v2.model.deployment_gates_evaluation_request_data_type import (
    DeploymentGatesEvaluationRequestDataType,
)

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ATTRIBUTES_IDENTIFIER = environ["DEPLOYMENT_GATE_DATA_ATTRIBUTES_IDENTIFIER"]

body = DeploymentGatesEvaluationRequest(
    data=DeploymentGatesEvaluationRequestData(
        attributes=DeploymentGatesEvaluationRequestAttributes(
            env="production",
            identifier=DEPLOYMENT_GATE_DATA_ATTRIBUTES_IDENTIFIER,
            service="my-service",
        ),
        type=DeploymentGatesEvaluationRequestDataType.DEPLOYMENT_GATES_EVALUATION_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["trigger_deployment_gates_evaluation"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.trigger_deployment_gates_evaluation(body=body)

    print(response)
