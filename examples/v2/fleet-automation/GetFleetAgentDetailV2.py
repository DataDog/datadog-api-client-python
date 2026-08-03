"""
Get detailed information about an agent returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.get_fleet_agent_detail_v2(
        agent_key="a1b2c3d4e5f67890a1b2c3d4e5f67890",
    )

    print(response)
