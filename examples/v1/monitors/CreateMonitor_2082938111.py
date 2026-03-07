"""
Create a monitor with aggregate filtered query variables returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_filtered_data_source import (
    MonitorFormulaAndFunctionAggregateFilteredDataSource,
)
from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_filtered_query_definition import (
    MonitorFormulaAndFunctionAggregateFilteredQueryDefinition,
)
from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_query_filter import (
    MonitorFormulaAndFunctionAggregateQueryFilter,
)
from datadog_api_client.v1.model.monitor_formula_and_function_metrics_data_source import (
    MonitorFormulaAndFunctionMetricsDataSource,
)
from datadog_api_client.v1.model.monitor_formula_and_function_metrics_query_definition import (
    MonitorFormulaAndFunctionMetricsQueryDefinition,
)
from datadog_api_client.v1.model.monitor_formula_and_function_reference_table_column import (
    MonitorFormulaAndFunctionReferenceTableColumn,
)
from datadog_api_client.v1.model.monitor_formula_and_function_reference_table_data_source import (
    MonitorFormulaAndFunctionReferenceTableDataSource,
)
from datadog_api_client.v1.model.monitor_formula_and_function_reference_table_query_definition import (
    MonitorFormulaAndFunctionReferenceTableQueryDefinition,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.QUERY_ALERT,
    query='formula("query1").rollup("sum").last("5m") > 100',
    message="test message",
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=100.0,
        ),
        variables=[
            MonitorFormulaAndFunctionAggregateFilteredQueryDefinition(
                data_source=MonitorFormulaAndFunctionAggregateFilteredDataSource.AGGREGATE_FILTERED_QUERY,
                name="query1",
                base_query=MonitorFormulaAndFunctionMetricsQueryDefinition(
                    data_source=MonitorFormulaAndFunctionMetricsDataSource.METRICS,
                    name="query1",
                    query="max:container.cpu.usage{*} by {kube_cluster_name}.rollup(max)",
                ),
                filter_query=MonitorFormulaAndFunctionReferenceTableQueryDefinition(
                    name="filter_query",
                    data_source=MonitorFormulaAndFunctionReferenceTableDataSource.REFERENCE_TABLE,
                    table_name="test_table",
                    columns=[
                        MonitorFormulaAndFunctionReferenceTableColumn(
                            name="cluster_name",
                        ),
                    ],
                ),
                filters=[
                    MonitorFormulaAndFunctionAggregateQueryFilter(
                        base_attribute="kube_cluster_name",
                        filter_attribute="cluster_name",
                    ),
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
