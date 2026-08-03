"""
Upgrade hosts returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi
from datadog_api_client.v2.model.fleet_deployment_package import FleetDeploymentPackage
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_v2_attributes import (
    FleetDeploymentPackageUpgradeV2Attributes,
)
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_v2_create import FleetDeploymentPackageUpgradeV2Create
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_v2_create_request import (
    FleetDeploymentPackageUpgradeV2CreateRequest,
)
from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType

body = FleetDeploymentPackageUpgradeV2CreateRequest(
    data=FleetDeploymentPackageUpgradeV2Create(
        attributes=FleetDeploymentPackageUpgradeV2Attributes(
            filter_query="env:prod AND service:example-fleet-automation",
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
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.create_fleet_deployment_upgrade_v2(body=body)

    print(response)
