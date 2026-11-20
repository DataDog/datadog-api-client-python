"""
Trigger a deployment gates evaluation with an inline bits deployment analysis rule returns "Accepted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from datadog_api_client.v2.model.deployment_gates_bits_deployment_analysis_rule import (
    DeploymentGatesBitsDeploymentAnalysisRule,
)
from datadog_api_client.v2.model.deployment_gates_bits_deployment_analysis_rule_options import (
    DeploymentGatesBitsDeploymentAnalysisRuleOptions,
)
from datadog_api_client.v2.model.deployment_gates_bits_deployment_analysis_rule_type import (
    DeploymentGatesBitsDeploymentAnalysisRuleType,
)
from datadog_api_client.v2.model.deployment_gates_evaluation_configuration import DeploymentGatesEvaluationConfiguration
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
            configuration=DeploymentGatesEvaluationConfiguration(
                dry_run=False,
                rules=[
                    DeploymentGatesBitsDeploymentAnalysisRule(
                        dry_run=False,
                        name="bits deployment analysis",
                        options=DeploymentGatesBitsDeploymentAnalysisRuleOptions(
                            duration=900,
                        ),
                        type=DeploymentGatesBitsDeploymentAnalysisRuleType.BITS_DEPLOYMENT_ANALYSIS,
                    ),
                ],
            ),
            env="production",
            identifier=DEPLOYMENT_GATE_DATA_ATTRIBUTES_IDENTIFIER,
            service="my-service",
        ),
        type=DeploymentGatesEvaluationRequestDataType.DEPLOYMENT_GATES_EVALUATION_REQUEST,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["trigger_deployment_gates_evaluation"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.trigger_deployment_gates_evaluation(body=body)

    print(response)
