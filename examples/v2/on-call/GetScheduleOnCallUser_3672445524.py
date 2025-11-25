"""
Get the schedule on-call user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.get_schedule_on_call_user(
        schedule_id=SCHEDULE_DATA_ID,
    )

    print(response)
