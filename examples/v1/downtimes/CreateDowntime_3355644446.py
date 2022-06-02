"""
Schedule a monitor downtime returns "OK" response
"""

from datetime import datetime
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

body = Downtime(
    message="Example-Schedule_a_monitor_downtime_returns_OK_response",
    start=int(datetime.now().timestamp()),
    timezone="Etc/UTC",
    scope=[
        "test:examplescheduleamonitordowntimereturnsokresponse",
    ],
    monitor_id=int(MONITOR_ID),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
