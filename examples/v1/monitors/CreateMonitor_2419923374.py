"""
Create a monitor with a metrics formula variable returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_metric_query_data_source import (
    MonitorFormulaAndFunctionMetricQueryDataSource,
)
from datadog_api_client.v1.model.monitor_formula_and_function_metric_query_definition import (
    MonitorFormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.QUERY_ALERT,
    query='formula("query1 / query2").rollup("avg").last("5m") > threshold',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical_query='formula("query1 / query2").rollup("p99").last("1w").multiplier(1.5)',
        ),
        variables=[
            MonitorFormulaAndFunctionMetricQueryDefinition(
                name="query1",
                data_source=MonitorFormulaAndFunctionMetricQueryDataSource.METRICS,
                query="sum:trace.http.request.errors{*}.as_count()",
            ),
            MonitorFormulaAndFunctionMetricQueryDefinition(
                name="query2",
                data_source=MonitorFormulaAndFunctionMetricQueryDataSource.METRICS,
                query="sum:trace.http.request.hits{*}.as_count()",
            ),
        ],
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
