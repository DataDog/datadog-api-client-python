"""
Create a Data Quality monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_data_source import (
    MonitorFormulaAndFunctionDataQualityDataSource,
)
from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_query_definition import (
    MonitorFormulaAndFunctionDataQualityQueryDefinition,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.DATA_QUALITY_ALERT,
    query='formula("query1").last("5m") > 100',
    message="Data quality alert triggered",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=100.0,
        ),
        variables=[
            MonitorFormulaAndFunctionDataQualityQueryDefinition(
                name="query1",
                data_source=MonitorFormulaAndFunctionDataQualityDataSource.DATA_QUALITY_METRICS,
                measure="row_count",
                filter="search for column where `database:production AND table:users`",
                group_by=[
                    "entity_id",
                ],
            ),
        ],
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
