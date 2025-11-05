"""
List all available Agent versions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
configuration.unstable_operations["list_fleet_agent_versions"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.list_fleet_agent_versions()

    print(response)
