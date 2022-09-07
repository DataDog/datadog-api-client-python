"""
Validate an existing monitor returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType
from datadog_api_client.v1.model.on_missing_data_option import OnMissingDataOption

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

body = Monitor(
    name="Example-Validate_an_existing_monitor_returns_OK_response",
    type=MonitorType.LOG_ALERT,
    query='logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplevalidateanexistingmonitorreturnsokresponse",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        enable_logs_sample=True,
        escalation_message="the situation has escalated",
        evaluation_delay=700,
        groupby_simple_monitor=True,
        include_tags=True,
        locked=False,
        new_host_delay=600,
        no_data_timeframe=None,
        notify_audit=False,
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
    response = api_instance.validate_existing_monitor(monitor_id=int(MONITOR_ID), body=body)

    print(response)
