"""
Schedule a downtime returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence

body = Downtime(
    message="Example-Schedule_a_downtime_returns_OK_response",
    start=int(datetime.now().timestamp()),
    timezone="Etc/UTC",
    scope=[
        "test:examplescheduleadowntimereturnsokresponse",
    ],
    recurrence=DowntimeRecurrence(
        type="weeks",
        period=1,
        week_days=[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
        ],
        until_date=int((datetime.now() + relativedelta(days=21)).timestamp()),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
