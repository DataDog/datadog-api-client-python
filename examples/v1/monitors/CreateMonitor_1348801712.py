"""
Create an LLM Observability monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.LLM_OBSERVABILITY_ALERT,
    query='llm-observability("*").rollup("count").last("2h") > 0',
    message="LLM observability alert triggered",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=0.0,
        ),
        include_tags=True,
        notify_audit=False,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
