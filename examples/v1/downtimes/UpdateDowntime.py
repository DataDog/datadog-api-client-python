"""
Update a downtime returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
from datadog_api_client.v1.model.notify_end_state import NotifyEndState
from datadog_api_client.v1.model.notify_end_type import NotifyEndType

# there is a valid "downtime" in the system
DOWNTIME_ID = environ["DOWNTIME_ID"]

body = Downtime(
    message="Example-Downtime-updated",
    mute_first_recovery_notification=True,
    notify_end_states=[
        NotifyEndState.ALERT,
        NotifyEndState.NO_DATA,
        NotifyEndState.WARN,
    ],
    notify_end_types=[
        NotifyEndType.CANCELED,
        NotifyEndType.EXPIRED,
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.update_downtime(downtime_id=int(DOWNTIME_ID), body=body)

    print(response)
