"""
Create a RUM formula and functions monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_event_aggregation import (
    MonitorFormulaAndFunctionEventAggregation,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition import (
    MonitorFormulaAndFunctionEventQueryDefinition,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_compute import (
    MonitorFormulaAndFunctionEventQueryDefinitionCompute,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_search import (
    MonitorFormulaAndFunctionEventQueryDefinitionSearch,
)
from datadog_api_client.v1.model.monitor_formula_and_function_events_data_source import (
    MonitorFormulaAndFunctionEventsDataSource,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Create_a_RUM_formula_and_functions_monitor_returns_OK_response",
    type=MonitorType.RUM_ALERT,
    query='formula("query2 / query1 * 100").last("15m") >= 0.8',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplecreatearumformulaandfunctionsmonitorreturnsokresponse",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=0.8,
        ),
        variables=[
            MonitorFormulaAndFunctionEventQueryDefinition(
                data_source=MonitorFormulaAndFunctionEventsDataSource.RUM,
                name="query2",
                search=MonitorFormulaAndFunctionEventQueryDefinitionSearch(
                    query="",
                ),
                indexes=[
                    "*",
                ],
                compute=MonitorFormulaAndFunctionEventQueryDefinitionCompute(
                    aggregation=MonitorFormulaAndFunctionEventAggregation.COUNT,
                ),
                group_by=[],
            ),
            MonitorFormulaAndFunctionEventQueryDefinition(
                data_source=MonitorFormulaAndFunctionEventsDataSource.RUM,
                name="query1",
                search=MonitorFormulaAndFunctionEventQueryDefinitionSearch(
                    query="status:error",
                ),
                indexes=[
                    "*",
                ],
                compute=MonitorFormulaAndFunctionEventQueryDefinitionCompute(
                    aggregation=MonitorFormulaAndFunctionEventAggregation.COUNT,
                ),
                group_by=[],
            ),
        ],
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
