"""
Schedule a downtime until date
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence

body = Downtime(
    message="Example-Schedule_a_downtime_until_date",
    recurrence=DowntimeRecurrence(
        period=1,
        type="weeks",
        until_date=int((datetime.now() + relativedelta(days=21)).timestamp()),
        week_days=[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
        ],
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
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
