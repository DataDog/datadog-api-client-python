"""
Create a monitor returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_type import MonitorType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.LOG_ALERT,
    query='logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    priority=3,
    restricted_roles=[
        ROLE_DATA_ID,
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
