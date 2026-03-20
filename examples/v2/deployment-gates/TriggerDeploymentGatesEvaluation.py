"""
Trigger a deployment gate evaluation returns "Accepted" response
"""

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

body = DeploymentGatesEvaluationRequest(
    data=DeploymentGatesEvaluationRequestData(
        attributes=DeploymentGatesEvaluationRequestAttributes(
            env="staging",
            identifier="pre-deploy",
            primary_tag="region:us-east-1",
            service="transaction-backend",
            version="v1.2.3",
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
