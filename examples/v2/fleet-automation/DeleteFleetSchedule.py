"""
Delete a schedule returns "Schedule successfully deleted." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["delete_fleet_schedule"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    api_instance.delete_fleet_schedule(
        id="id",
    )
