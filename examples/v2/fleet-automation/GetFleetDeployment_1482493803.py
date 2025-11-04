"""
Get a deployment by ID returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

# there is a valid "deployment" in the system
DEPLOYMENT_ID = environ["DEPLOYMENT_ID"]

configuration = Configuration()
configuration.unstable_operations["get_fleet_deployment"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.get_fleet_deployment(
        deployment_id=DEPLOYMENT_ID,
    )

    print(response)
