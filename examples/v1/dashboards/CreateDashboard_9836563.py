"""
Create a geomap widget with conditional formats and text formats
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.dashboard_reflow_type import DashboardReflowType
from datadog_api_client.v1.model.formula_and_function_event_aggregation import FormulaAndFunctionEventAggregation
from datadog_api_client.v1.model.formula_and_function_event_query_definition import (
    FormulaAndFunctionEventQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_event_query_definition_compute import (
    FormulaAndFunctionEventQueryDefinitionCompute,
)
from datadog_api_client.v1.model.formula_and_function_event_query_definition_search import (
    FormulaAndFunctionEventQueryDefinitionSearch,
)
from datadog_api_client.v1.model.formula_and_function_events_data_source import FormulaAndFunctionEventsDataSource
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.formula_type import FormulaType
from datadog_api_client.v1.model.geomap_widget_definition import GeomapWidgetDefinition
from datadog_api_client.v1.model.geomap_widget_definition_style import GeomapWidgetDefinitionStyle
from datadog_api_client.v1.model.geomap_widget_definition_type import GeomapWidgetDefinitionType
from datadog_api_client.v1.model.geomap_widget_definition_view import GeomapWidgetDefinitionView
from datadog_api_client.v1.model.geomap_widget_request import GeomapWidgetRequest
from datadog_api_client.v1.model.geomap_widget_request_style import GeomapWidgetRequestStyle
from datadog_api_client.v1.model.list_stream_column import ListStreamColumn
from datadog_api_client.v1.model.list_stream_column_width import ListStreamColumnWidth
from datadog_api_client.v1.model.list_stream_query import ListStreamQuery
from datadog_api_client.v1.model.list_stream_source import ListStreamSource
from datadog_api_client.v1.model.table_widget_text_format_match import TableWidgetTextFormatMatch
from datadog_api_client.v1.model.table_widget_text_format_match_type import TableWidgetTextFormatMatchType
from datadog_api_client.v1.model.table_widget_text_format_palette import TableWidgetTextFormatPalette
from datadog_api_client.v1.model.table_widget_text_format_rule import TableWidgetTextFormatRule
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_comparator import WidgetComparator
from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_formula_sort import WidgetFormulaSort
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_palette import WidgetPalette
from datadog_api_client.v1.model.widget_sort import WidgetSort
from datadog_api_client.v1.model.widget_sort_by import WidgetSortBy

body = Dashboard(
    title="Example-Dashboard",
    description="Example-Dashboard",
    widgets=[
        Widget(
            definition=GeomapWidgetDefinition(
                title="Log Count by Service and Source",
                type=GeomapWidgetDefinitionType.GEOMAP,
                requests=[
                    GeomapWidgetRequest(
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                        queries=[
                            FormulaAndFunctionEventQueryDefinition(
                                data_source=FormulaAndFunctionEventsDataSource.RUM,
                                name="query1",
                                search=FormulaAndFunctionEventQueryDefinitionSearch(
                                    query="@type:session",
                                ),
                                indexes=[
                                    "*",
                                ],
                                compute=FormulaAndFunctionEventQueryDefinitionCompute(
                                    aggregation=FormulaAndFunctionEventAggregation.COUNT,
                                ),
                                group_by=[],
                            ),
                        ],
                        conditional_formats=[
                            WidgetConditionalFormat(
                                comparator=WidgetComparator.GREATER_THAN,
                                value=1000.0,
                                palette=WidgetPalette.WHITE_ON_GREEN,
                            ),
                        ],
                        formulas=[
                            WidgetFormula(
                                formula="query1",
                            ),
                        ],
                        sort=WidgetSortBy(
                            count=250,
                            order_by=[
                                WidgetFormulaSort(
                                    type=FormulaType.FORMULA,
                                    index=0,
                                    order=WidgetSort.DESCENDING,
                                ),
                            ],
                        ),
                    ),
                    GeomapWidgetRequest(
                        response_format=FormulaAndFunctionResponseFormat.EVENT_LIST,
                        query=ListStreamQuery(
                            data_source=ListStreamSource.LOGS_STREAM,
                            query_string="",
                            indexes=[],
                            storage="hot",
                        ),
                        columns=[
                            ListStreamColumn(
                                field="@network.client.geoip.location.latitude",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="@network.client.geoip.location.longitude",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="@network.client.geoip.country.iso_code",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="@network.client.geoip.subdivision.name",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                        ],
                        style=GeomapWidgetRequestStyle(
                            color_by="status",
                        ),
                        text_formats=[
                            TableWidgetTextFormatRule(
                                match=TableWidgetTextFormatMatch(
                                    type=TableWidgetTextFormatMatchType.IS,
                                    value="error",
                                ),
                                palette=TableWidgetTextFormatPalette.WHITE_ON_RED,
                            ),
                        ],
                    ),
                ],
                style=GeomapWidgetDefinitionStyle(
                    palette="hostmap_blues",
                    palette_flip=False,
                ),
                view=GeomapWidgetDefinitionView(
                    focus="NORTH_AMERICA",
                ),
            ),
            layout=WidgetLayout(
                x=0,
                y=0,
                width=12,
                height=6,
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.ORDERED,
    notify_list=[],
    reflow_type=DashboardReflowType.FIXED,
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
