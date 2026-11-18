"""
Get a fleet access scope returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

# there is a valid "fleet_access_scope" in the system
FLEET_ACCESS_SCOPE_ID = environ["FLEET_ACCESS_SCOPE_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_fleet_access_scope"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.get_fleet_access_scope(
        access_scope_id=FLEET_ACCESS_SCOPE_ID,
    )

    print(response)
