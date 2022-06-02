"""
Update a downtime returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime

# there is a valid "downtime" in the system
DOWNTIME_ID = environ["DOWNTIME_ID"]

body = Downtime(
    message="Example-Update_a_downtime_returns_OK_response-updated",
    mute_first_recovery_notification=True,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.update_downtime(downtime_id=int(DOWNTIME_ID), body=body)

    print(response)
