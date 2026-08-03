"""
Get a schedule by ID returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi

# there is a valid "fleet_schedule" in the system
SCHEDULE_ID = environ["SCHEDULE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.get_fleet_schedule_v2(
        id=SCHEDULE_ID,
    )

    print(response)
