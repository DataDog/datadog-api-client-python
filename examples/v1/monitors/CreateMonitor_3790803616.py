"""
Create a ci-pipelines monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Create_a_ci_pipelines_monitor_returns_OK_response",
    type=MonitorType.CI_PIPELINES_ALERT,
    query='ci-pipelines("ci_level:pipeline @git.branch:staging* @ci.status:error").rollup("count").by("@git.branch,@ci.pipeline.name").last("5m") >= 1',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplecreateacipipelinesmonitorreturnsokresponse",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=1.0,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
