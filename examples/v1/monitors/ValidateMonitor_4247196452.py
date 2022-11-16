"""
Validate a multi-alert monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType
from datadog_api_client.v1.model.on_missing_data_option import OnMissingDataOption

body = Monitor(
    name="Example-Validate_a_multi_alert_monitor_returns_OK_response",
    type=MonitorType.LOG_ALERT,
    query='logs("service:foo AND type:error").index("main").rollup("count").by("source,status").last("5m") > 2',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplevalidateamultialertmonitorreturnsokresponse",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        enable_logs_sample=True,
        escalation_message="the situation has escalated",
        evaluation_delay=700,
        group_retention_duration="2d",
        groupby_simple_monitor=False,
        include_tags=True,
        locked=False,
        new_host_delay=600,
        no_data_timeframe=None,
        notify_audit=False,
        notify_by=[
            "status",
        ],
        notify_no_data=False,
        on_missing_data=OnMissingDataOption.SHOW_AND_NOTIFY_NO_DATA,
        renotify_interval=60,
        require_full_window=True,
        timeout_h=24,
        thresholds=MonitorThresholds(
            critical=2.0,
            warning=1.0,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.validate_monitor(body=body)

    print(response)
