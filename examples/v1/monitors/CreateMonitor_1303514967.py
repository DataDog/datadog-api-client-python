"""
Create a Cost Monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_cost_aggregator import (
    MonitorFormulaAndFunctionCostAggregator,
)
from datadog_api_client.v1.model.monitor_formula_and_function_cost_data_source import (
    MonitorFormulaAndFunctionCostDataSource,
)
from datadog_api_client.v1.model.monitor_formula_and_function_cost_query_definition import (
    MonitorFormulaAndFunctionCostQueryDefinition,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example Monitor",
    type=MonitorType.COST_ALERT,
    query='formula("exclude_null(query1)").last("7d").anomaly(direction="above", threshold=10) >= 5',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=5.0,
            warning=3.0,
        ),
        variables=[
            MonitorFormulaAndFunctionCostQueryDefinition(
                data_source=MonitorFormulaAndFunctionCostDataSource.CLOUD_COST,
                query="sum:aws.cost.net.amortized.shared.resources.allocated{aws_product IN (amplify ,athena, backup, bedrock ) } by {aws_product}.rollup(sum, 86400)",
                name="query1",
                aggregator=MonitorFormulaAndFunctionCostAggregator.SUM,
            ),
        ],
        include_tags=True,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
