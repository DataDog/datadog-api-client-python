"""
Create a new dashboard with topology_map custom widget
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_metric_aggregation import FormulaAndFunctionMetricAggregation
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.number_format_unit_canonical import NumberFormatUnitCanonical
from datadog_api_client.v1.model.number_format_unit_scale_type import NumberFormatUnitScaleType
from datadog_api_client.v1.model.topology_map_inline_column_kind_scalar import TopologyMapInlineColumnKindScalar
from datadog_api_client.v1.model.topology_map_inline_column_kind_string import TopologyMapInlineColumnKindString
from datadog_api_client.v1.model.topology_map_inline_data import TopologyMapInlineData
from datadog_api_client.v1.model.topology_map_inline_edge_column import TopologyMapInlineEdgeColumn
from datadog_api_client.v1.model.topology_map_inline_edge_column_id import TopologyMapInlineEdgeColumnId
from datadog_api_client.v1.model.topology_map_inline_edges_data import TopologyMapInlineEdgesData
from datadog_api_client.v1.model.topology_map_inline_node_id_column import TopologyMapInlineNodeIdColumn
from datadog_api_client.v1.model.topology_map_inline_node_id_column_id import TopologyMapInlineNodeIdColumnId
from datadog_api_client.v1.model.topology_map_inline_node_string_column import TopologyMapInlineNodeStringColumn
from datadog_api_client.v1.model.topology_map_inline_node_string_column_id import TopologyMapInlineNodeStringColumnId
from datadog_api_client.v1.model.topology_map_inline_node_value_column import TopologyMapInlineNodeValueColumn
from datadog_api_client.v1.model.topology_map_inline_node_value_column_meta import TopologyMapInlineNodeValueColumnMeta
from datadog_api_client.v1.model.topology_map_inline_nodes_data import TopologyMapInlineNodesData
from datadog_api_client.v1.model.topology_map_layout import TopologyMapLayout
from datadog_api_client.v1.model.topology_map_layout_direction import TopologyMapLayoutDirection
from datadog_api_client.v1.model.topology_map_layout_type import TopologyMapLayoutType
from datadog_api_client.v1.model.topology_map_widget_definition_custom import TopologyMapWidgetDefinitionCustom
from datadog_api_client.v1.model.topology_map_widget_definition_type import TopologyMapWidgetDefinitionType
from datadog_api_client.v1.model.topology_request_custom import TopologyRequestCustom
from datadog_api_client.v1.model.topology_request_custom_projection import TopologyRequestCustomProjection
from datadog_api_client.v1.model.topology_request_custom_projection_dimension import (
    TopologyRequestCustomProjectionDimension,
)
from datadog_api_client.v1.model.topology_request_custom_projection_type import TopologyRequestCustomProjectionType
from datadog_api_client.v1.model.topology_request_custom_response_format import TopologyRequestCustomResponseFormat
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    description="",
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=15,
            ),
            definition=TopologyMapWidgetDefinitionCustom(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=TopologyMapWidgetDefinitionType.TOPOLOGY_MAP,
                layout=TopologyMapLayout(
                    type=TopologyMapLayoutType.HIERARCHICAL,
                    direction=TopologyMapLayoutDirection.LEFT_TO_RIGHT,
                ),
                data=TopologyMapInlineData(
                    nodes=TopologyMapInlineNodesData(
                        columns=[
                            TopologyMapInlineNodeIdColumn(
                                kind=TopologyMapInlineColumnKindString.STRING,
                                id=TopologyMapInlineNodeIdColumnId.ID,
                                values=[
                                    "service:web",
                                    "service:db",
                                ],
                            ),
                            TopologyMapInlineNodeStringColumn(
                                kind=TopologyMapInlineColumnKindString.STRING,
                                id=TopologyMapInlineNodeStringColumnId.SUBTITLE,
                                values=[
                                    "api-team",
                                    None,
                                ],
                            ),
                            TopologyMapInlineNodeValueColumn(
                                kind=TopologyMapInlineColumnKindScalar.SCALAR,
                                id="values[1]",
                                values=[
                                    1.5,
                                    None,
                                ],
                                meta=TopologyMapInlineNodeValueColumnMeta(
                                    unit=NumberFormatUnitCanonical(
                                        type=NumberFormatUnitScaleType.CANONICAL_UNIT,
                                        unit_name="second",
                                    ),
                                ),
                            ),
                        ],
                    ),
                    edges=TopologyMapInlineEdgesData(
                        columns=[
                            TopologyMapInlineEdgeColumn(
                                kind=TopologyMapInlineColumnKindString.STRING,
                                id=TopologyMapInlineEdgeColumnId.SOURCE,
                                values=[
                                    "service:web",
                                ],
                            ),
                            TopologyMapInlineEdgeColumn(
                                kind=TopologyMapInlineColumnKindString.STRING,
                                id=TopologyMapInlineEdgeColumnId.TARGET,
                                values=[
                                    "service:db",
                                ],
                            ),
                        ],
                    ),
                ),
                requests=[
                    TopologyRequestCustom(
                        response_format=TopologyRequestCustomResponseFormat.SCALAR,
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="a",
                                query="avg:system.cpu.user{*} by {service}",
                                aggregator=FormulaAndFunctionMetricAggregation.AVG,
                            ),
                        ],
                        formulas=[
                            WidgetFormula(
                                formula="a",
                            ),
                        ],
                        projection=TopologyRequestCustomProjection(
                            type=TopologyRequestCustomProjectionType.CUSTOM_TOPOLOGY_MAP_NODE,
                            dimensions=[
                                TopologyRequestCustomProjectionDimension(
                                    column="a",
                                    dimension="values[0]",
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.FREE,
    notify_list=[],
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
