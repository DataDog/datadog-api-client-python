"""
Delete an override returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

# there is a valid "override" in the system
OVERRIDE_DATA_0_ID = environ["OVERRIDE_DATA_0_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    api_instance.delete_on_call_schedule_override(
        schedule_id=SCHEDULE_DATA_ID,
        override_id=OVERRIDE_DATA_0_ID,
    )
