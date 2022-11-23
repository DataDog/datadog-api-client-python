"""
Create a metric monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_options_scheduling_options import MonitorOptionsSchedulingOptions
from datadog_api_client.v1.model.monitor_options_scheduling_options_evaluation_window import (
    MonitorOptionsSchedulingOptionsEvaluationWindow,
)
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Create_a_metric_monitor_returns_OK_response",
    type=MonitorType.METRIC_ALERT,
    query="avg(current_1d):avg:system.load.5{*} > 0.5",
    message="some message Notify: @hipchat-channel",
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=0.5,
        ),
        scheduling_options=MonitorOptionsSchedulingOptions(
            evaluation_window=MonitorOptionsSchedulingOptionsEvaluationWindow(
                day_starts="04:00",
                month_starts=1,
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
