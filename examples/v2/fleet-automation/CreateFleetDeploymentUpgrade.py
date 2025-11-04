"""
Upgrade hosts returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi
from datadog_api_client.v2.model.fleet_deployment_package import FleetDeploymentPackage
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_attributes import (
    FleetDeploymentPackageUpgradeAttributes,
)
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_create import FleetDeploymentPackageUpgradeCreate
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_create_request import (
    FleetDeploymentPackageUpgradeCreateRequest,
)
from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType

body = FleetDeploymentPackageUpgradeCreateRequest(
    data=FleetDeploymentPackageUpgradeCreate(
        attributes=FleetDeploymentPackageUpgradeAttributes(
            filter_query="env:prod AND service:web",
            target_packages=[
                FleetDeploymentPackage(
                    name="datadog-agent",
                    version="7.52.0",
                ),
            ],
        ),
        type=FleetDeploymentResourceType.DEPLOYMENT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_fleet_deployment_upgrade"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.create_fleet_deployment_upgrade(body=body)

    print(response)
