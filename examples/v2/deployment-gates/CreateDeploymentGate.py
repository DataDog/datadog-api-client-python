"""
Create deployment gate returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from datadog_api_client.v2.model.create_deployment_gate_params import CreateDeploymentGateParams
from datadog_api_client.v2.model.create_deployment_gate_params_data import CreateDeploymentGateParamsData
from datadog_api_client.v2.model.create_deployment_gate_params_data_attributes import (
    CreateDeploymentGateParamsDataAttributes,
)
from datadog_api_client.v2.model.deployment_gate_data_type import DeploymentGateDataType

body = CreateDeploymentGateParams(
    data=CreateDeploymentGateParamsData(
        attributes=CreateDeploymentGateParamsDataAttributes(
            dry_run=False,
            env="production",
            identifier="my-gate-1",
            service="my-service",
        ),
        type=DeploymentGateDataType.DEPLOYMENT_GATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_deployment_gate"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.create_deployment_gate(body=body)

    print(response)
