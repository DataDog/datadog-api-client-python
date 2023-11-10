"""
Create a metric monitor with a custom schedule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_options_custom_schedule import MonitorOptionsCustomSchedule
from datadog_api_client.v1.model.monitor_options_custom_schedule_recurrence import (
    MonitorOptionsCustomScheduleRecurrence,
)
from datadog_api_client.v1.model.monitor_options_scheduling_options import MonitorOptionsSchedulingOptions
from datadog_api_client.v1.model.monitor_options_scheduling_options_evaluation_window import (
    MonitorOptionsSchedulingOptionsEvaluationWindow,
)
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    message="some message Notify: @hipchat-channel",
    name="Example-Monitor",
    query="avg(current_1mo):avg:system.load.5{*} > 0.5",
    tags=[],
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=0.5,
        ),
        notify_audit=False,
        include_tags=False,
        scheduling_options=MonitorOptionsSchedulingOptions(
            evaluation_window=MonitorOptionsSchedulingOptionsEvaluationWindow(
                day_starts="04:00",
                month_starts=1,
            ),
            custom_schedule=MonitorOptionsCustomSchedule(
                recurrences=[
                    MonitorOptionsCustomScheduleRecurrence(
                        rrule="FREQ=DAILY;INTERVAL=1",
                        timezone="America/Los_Angeles",
                        start="2024-10-26T09:13:00",
                    ),
                ],
            ),
        ),
    ),
    type=MonitorType.QUERY_ALERT,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
