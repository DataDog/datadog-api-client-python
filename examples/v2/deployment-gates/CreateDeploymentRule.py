"""
Create deployment rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from datadog_api_client.v2.model.create_deployment_rule_params import CreateDeploymentRuleParams
from datadog_api_client.v2.model.create_deployment_rule_params_data import CreateDeploymentRuleParamsData
from datadog_api_client.v2.model.create_deployment_rule_params_data_attributes import (
    CreateDeploymentRuleParamsDataAttributes,
)
from datadog_api_client.v2.model.deployment_rule_data_type import DeploymentRuleDataType
from datadog_api_client.v2.model.deployment_rule_options_faulty_deployment_detection import (
    DeploymentRuleOptionsFaultyDeploymentDetection,
)

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

body = CreateDeploymentRuleParams(
    data=CreateDeploymentRuleParamsData(
        attributes=CreateDeploymentRuleParamsDataAttributes(
            dry_run=False,
            name="My deployment rule",
            options=DeploymentRuleOptionsFaultyDeploymentDetection(
                excluded_resources=[],
            ),
            type="faulty_deployment_detection",
        ),
        type=DeploymentRuleDataType.DEPLOYMENT_RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_deployment_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.create_deployment_rule(gate_id=DEPLOYMENT_GATE_DATA_ID, body=body)

    print(response)
