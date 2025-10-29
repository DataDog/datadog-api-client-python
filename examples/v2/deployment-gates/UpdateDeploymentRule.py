"""
Update deployment rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from datadog_api_client.v2.model.deployment_rule_data_type import DeploymentRuleDataType
from datadog_api_client.v2.model.deployment_rule_options_faulty_deployment_detection import (
    DeploymentRuleOptionsFaultyDeploymentDetection,
)
from datadog_api_client.v2.model.update_deployment_rule_params import UpdateDeploymentRuleParams
from datadog_api_client.v2.model.update_deployment_rule_params_data import UpdateDeploymentRuleParamsData
from datadog_api_client.v2.model.update_deployment_rule_params_data_attributes import (
    UpdateDeploymentRuleParamsDataAttributes,
)

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

# there is a valid "deployment_rule" in the system
DEPLOYMENT_RULE_DATA_ID = environ["DEPLOYMENT_RULE_DATA_ID"]

body = UpdateDeploymentRuleParams(
    data=UpdateDeploymentRuleParamsData(
        attributes=UpdateDeploymentRuleParamsDataAttributes(
            dry_run=False,
            name="Updated deployment rule",
            options=DeploymentRuleOptionsFaultyDeploymentDetection(
                excluded_resources=[],
            ),
        ),
        type=DeploymentRuleDataType.DEPLOYMENT_RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_deployment_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.update_deployment_rule(
        gate_id=DEPLOYMENT_GATE_DATA_ID, id=DEPLOYMENT_RULE_DATA_ID, body=body
    )

    print(response)
