"""
Cancel a deployment returns "Deployment successfully canceled." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["cancel_fleet_deployment"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    api_instance.cancel_fleet_deployment(
        deployment_id="deployment_id",
    )
