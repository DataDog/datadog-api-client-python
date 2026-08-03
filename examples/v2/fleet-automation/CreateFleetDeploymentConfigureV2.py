"""
Create a configuration deployment returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi
from datadog_api_client.v2.model.fleet_deployment_configure_v2_attributes import FleetDeploymentConfigureV2Attributes
from datadog_api_client.v2.model.fleet_deployment_configure_v2_create import FleetDeploymentConfigureV2Create
from datadog_api_client.v2.model.fleet_deployment_configure_v2_create_request import (
    FleetDeploymentConfigureV2CreateRequest,
)
from datadog_api_client.v2.model.fleet_deployment_file_op import FleetDeploymentFileOp
from datadog_api_client.v2.model.fleet_deployment_operation import FleetDeploymentOperation
from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType

body = FleetDeploymentConfigureV2CreateRequest(
    data=FleetDeploymentConfigureV2Create(
        attributes=FleetDeploymentConfigureV2Attributes(
            config_operations=[
                FleetDeploymentOperation(
                    file_op=FleetDeploymentFileOp.MERGE_PATCH,
                    file_path="/datadog.yaml",
                    patch=dict([("log_level", "info")]),
                ),
            ],
            dry_run=True,
            filter_query="env:prod AND service:example-fleet-automation",
        ),
        type=FleetDeploymentResourceType.DEPLOYMENT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.create_fleet_deployment_configure_v2(body=body)

    print(response)
