"""
Create a new dashboard with query_table widget and text formatting
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.formula_and_function_metric_aggregation import FormulaAndFunctionMetricAggregation
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition
from datadog_api_client.v1.model.table_widget_definition_type import TableWidgetDefinitionType
from datadog_api_client.v1.model.table_widget_has_search_bar import TableWidgetHasSearchBar
from datadog_api_client.v1.model.table_widget_request import TableWidgetRequest
from datadog_api_client.v1.model.table_widget_text_format_match import TableWidgetTextFormatMatch
from datadog_api_client.v1.model.table_widget_text_format_match_type import TableWidgetTextFormatMatchType
from datadog_api_client.v1.model.table_widget_text_format_palette import TableWidgetTextFormatPalette
from datadog_api_client.v1.model.table_widget_text_format_replace_all import TableWidgetTextFormatReplaceAll
from datadog_api_client.v1.model.table_widget_text_format_replace_all_type import TableWidgetTextFormatReplaceAllType
from datadog_api_client.v1.model.table_widget_text_format_rule import TableWidgetTextFormatRule
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    description="",
    widgets=[
        Widget(
            definition=TableWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=TableWidgetDefinitionType.QUERY_TABLE,
                requests=[
                    TableWidgetRequest(
                        queries=[
                            FormulaAndFunctionMetricQueryDefinition(
                                aggregator=FormulaAndFunctionMetricAggregation.AVG,
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query1",
                                query="avg:aws.stream.globalaccelerator.processed_bytes_in{*} by {aws_account,acceleratoripaddress}",
                            ),
                            FormulaAndFunctionMetricQueryDefinition(
                                aggregator=FormulaAndFunctionMetricAggregation.AVG,
                                data_source=FormulaAndFunctionMetricDataSource.METRICS,
                                name="query2",
                                query="avg:aws.stream.globalaccelerator.processed_bytes_out{*} by {aws_account,acceleratoripaddress}",
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                        text_formats=[
                            [
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.IS,
                                        value="fruit",
                                    ),
                                    palette=TableWidgetTextFormatPalette.WHITE_ON_RED,
                                    replace=TableWidgetTextFormatReplaceAll(
                                        type=TableWidgetTextFormatReplaceAllType.ALL,
                                        _with="vegetable",
                                    ),
                                ),
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.IS,
                                        value="animal",
                                    ),
                                    palette=TableWidgetTextFormatPalette.CUSTOM_BG,
                                    custom_bg_color="#632ca6",
                                ),
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.IS,
                                        value="robot",
                                    ),
                                    palette=TableWidgetTextFormatPalette.RED_ON_WHITE,
                                ),
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.IS,
                                        value="ai",
                                    ),
                                    palette=TableWidgetTextFormatPalette.YELLOW_ON_WHITE,
                                ),
                            ],
                            [
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.IS_NOT,
                                        value="xyz",
                                    ),
                                    palette=TableWidgetTextFormatPalette.WHITE_ON_YELLOW,
                                ),
                            ],
                            [
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.CONTAINS,
                                        value="test",
                                    ),
                                    palette=TableWidgetTextFormatPalette.WHITE_ON_GREEN,
                                    replace=TableWidgetTextFormatReplaceAll(
                                        type=TableWidgetTextFormatReplaceAllType.ALL,
                                        _with="vegetable",
                                    ),
                                ),
                            ],
                            [
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.DOES_NOT_CONTAIN,
                                        value="blah",
                                    ),
                                    palette=TableWidgetTextFormatPalette.BLACK_ON_LIGHT_RED,
                                ),
                            ],
                            [
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.STARTS_WITH,
                                        value="abc",
                                    ),
                                    palette=TableWidgetTextFormatPalette.BLACK_ON_LIGHT_YELLOW,
                                ),
                            ],
                            [
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.ENDS_WITH,
                                        value="xyz",
                                    ),
                                    palette=TableWidgetTextFormatPalette.BLACK_ON_LIGHT_GREEN,
                                ),
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.ENDS_WITH,
                                        value="zzz",
                                    ),
                                    palette=TableWidgetTextFormatPalette.GREEN_ON_WHITE,
                                ),
                                TableWidgetTextFormatRule(
                                    match=TableWidgetTextFormatMatch(
                                        type=TableWidgetTextFormatMatchType.IS,
                                        value="animal",
                                    ),
                                    palette=TableWidgetTextFormatPalette.CUSTOM_TEXT,
                                    custom_fg_color="#632ca6",
                                ),
                            ],
                        ],
                        formulas=[],
                    ),
                ],
                has_search_bar=TableWidgetHasSearchBar.NEVER,
            ),
            layout=WidgetLayout(
                x=0,
                y=0,
                width=4,
                height=4,
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.FREE,
    notify_list=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
