"""
Create a monitor with aggregate augmented query variables returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_augmented_data_source import (
    MonitorFormulaAndFunctionAggregateAugmentedDataSource,
)
from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_augmented_query_definition import (
    MonitorFormulaAndFunctionAggregateAugmentedQueryDefinition,
)
from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_query_join_condition import (
    MonitorFormulaAndFunctionAggregateQueryJoinCondition,
)
from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_query_join_type import (
    MonitorFormulaAndFunctionAggregateQueryJoinType,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_aggregation import (
    MonitorFormulaAndFunctionEventAggregation,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_compute import (
    MonitorFormulaAndFunctionEventQueryDefinitionCompute,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_group_by import (
    MonitorFormulaAndFunctionEventQueryGroupBy,
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
    query='formula("query1").rollup("sum").last("5m") > 124',
    message="test message",
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=124.0,
        ),
        variables=[
            MonitorFormulaAndFunctionAggregateAugmentedQueryDefinition(
                data_source=MonitorFormulaAndFunctionAggregateAugmentedDataSource.AGGREGATE_AUGMENTED_QUERY,
                name="query1",
                group_by=[
                    MonitorFormulaAndFunctionEventQueryGroupBy(
                        facet="org_id",
                    ),
                    MonitorFormulaAndFunctionEventQueryGroupBy(
                        facet="name",
                    ),
                ],
                compute=[
                    MonitorFormulaAndFunctionEventQueryDefinitionCompute(
                        name="compute_result",
                        aggregation=MonitorFormulaAndFunctionEventAggregation.MAX,
                    ),
                ],
                augment_query=MonitorFormulaAndFunctionReferenceTableQueryDefinition(
                    name="filter_query",
                    data_source=MonitorFormulaAndFunctionReferenceTableDataSource.REFERENCE_TABLE,
                    table_name="test_table",
                    columns=[
                        MonitorFormulaAndFunctionReferenceTableColumn(
                            name="org_id",
                        ),
                        MonitorFormulaAndFunctionReferenceTableColumn(
                            name="name",
                        ),
                    ],
                ),
                base_query=MonitorFormulaAndFunctionMetricsQueryDefinition(
                    data_source=MonitorFormulaAndFunctionMetricsDataSource.METRICS,
                    name="query1",
                    query="avg:dd{*} by {org_id}.as_count()",
                ),
                join_condition=MonitorFormulaAndFunctionAggregateQueryJoinCondition(
                    augment_attribute="org_id",
                    base_attribute="org_id",
                    join_type=MonitorFormulaAndFunctionAggregateQueryJoinType.INNER,
                ),
            ),
        ],
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
