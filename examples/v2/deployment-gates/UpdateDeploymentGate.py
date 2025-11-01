"""
Update deployment gate returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from datadog_api_client.v2.model.deployment_gate_data_type import DeploymentGateDataType
from datadog_api_client.v2.model.update_deployment_gate_params import UpdateDeploymentGateParams
from datadog_api_client.v2.model.update_deployment_gate_params_data import UpdateDeploymentGateParamsData
from datadog_api_client.v2.model.update_deployment_gate_params_data_attributes import (
    UpdateDeploymentGateParamsDataAttributes,
)

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

body = UpdateDeploymentGateParams(
    data=UpdateDeploymentGateParamsData(
        attributes=UpdateDeploymentGateParamsDataAttributes(
            dry_run=False,
        ),
        id="12345678-1234-1234-1234-123456789012",
        type=DeploymentGateDataType.DEPLOYMENT_GATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_deployment_gate"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.update_deployment_gate(id=DEPLOYMENT_GATE_DATA_ID, body=body)

    print(response)
