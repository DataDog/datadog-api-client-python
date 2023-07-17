"""
Schedule a downtime once a year
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence
from datadog_api_client.v1.model.notify_end_state import NotifyEndState
from datadog_api_client.v1.model.notify_end_type import NotifyEndType

body = Downtime(
    message="Example-Downtime",
    recurrence=DowntimeRecurrence(
        period=1,
        type="years",
    ),
    scope=[
        "*",
    ],
    start=int(datetime.now().timestamp()),
    end=int((datetime.now() + relativedelta(hours=1)).timestamp()),
    timezone="Etc/UTC",
    mute_first_recovery_notification=True,
    monitor_tags=[
        "tag0",
    ],
    notify_end_states=[
        NotifyEndState.ALERT,
        NotifyEndState.WARN,
    ],
    notify_end_types=[
        NotifyEndType.EXPIRED,
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
