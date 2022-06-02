"""
Edit a monitor returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_update_request import MonitorUpdateRequest

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]
MONITOR_NAME = environ["MONITOR_NAME"]

body = MonitorUpdateRequest(
    name="My monitor-updated",
    options=MonitorOptions(
        evaluation_delay=None,
        new_group_delay=600,
        new_host_delay=None,
        renotify_interval=None,
        thresholds=MonitorThresholds(
            critical=2.0,
            warning=None,
        ),
        timeout_h=None,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.update_monitor(monitor_id=int(MONITOR_ID), body=body)

    print(response)
