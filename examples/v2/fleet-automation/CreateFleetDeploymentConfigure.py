"""
Create a configuration deployment returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi
from datadog_api_client.v2.model.fleet_deployment_configure_attributes import FleetDeploymentConfigureAttributes
from datadog_api_client.v2.model.fleet_deployment_configure_create import FleetDeploymentConfigureCreate
from datadog_api_client.v2.model.fleet_deployment_configure_create_request import FleetDeploymentConfigureCreateRequest
from datadog_api_client.v2.model.fleet_deployment_file_op import FleetDeploymentFileOp
from datadog_api_client.v2.model.fleet_deployment_operation import FleetDeploymentOperation
from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType

body = FleetDeploymentConfigureCreateRequest(
    data=FleetDeploymentConfigureCreate(
        attributes=FleetDeploymentConfigureAttributes(
            config_operations=[
                FleetDeploymentOperation(
                    file_op=FleetDeploymentFileOp.MERGE_PATCH,
                    file_path="/datadog.yaml",
                    patch=dict([("apm_config", "{'enabled': True}"), ("log_level", "debug"), ("logs_enabled", "True")]),
                ),
            ],
            filter_query="env:prod AND service:web",
        ),
        type=FleetDeploymentResourceType.DEPLOYMENT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_fleet_deployment_configure"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.create_fleet_deployment_configure(body=body)

    print(response)
