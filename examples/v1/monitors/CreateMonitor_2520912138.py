"""
Create a ci-tests monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Create_a_ci_tests_monitor_returns_OK_response",
    type=MonitorType.CI_TESTS_ALERT,
    query='ci-tests("type:test @git.branch:staging* @test.status:fail").rollup("count").by("@test.name").last("5m") >= 1',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplecreateacitestsmonitorreturnsokresponse",
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
