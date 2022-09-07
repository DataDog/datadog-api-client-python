"""
Create a new dashboard with geomap widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
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
from datadog_api_client.v1.model.formula_and_function_event_query_group_by import FormulaAndFunctionEventQueryGroupBy
from datadog_api_client.v1.model.formula_and_function_event_query_group_by_sort import (
    FormulaAndFunctionEventQueryGroupBySort,
)
from datadog_api_client.v1.model.formula_and_function_events_data_source import FormulaAndFunctionEventsDataSource
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.geomap_widget_definition import GeomapWidgetDefinition
from datadog_api_client.v1.model.geomap_widget_definition_style import GeomapWidgetDefinitionStyle
from datadog_api_client.v1.model.geomap_widget_definition_type import GeomapWidgetDefinitionType
from datadog_api_client.v1.model.geomap_widget_definition_view import GeomapWidgetDefinitionView
from datadog_api_client.v1.model.geomap_widget_request import GeomapWidgetRequest
from datadog_api_client.v1.model.query_sort_order import QuerySortOrder
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_formula_limit import WidgetFormulaLimit
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

body = Dashboard(
    title="Example-Create_a_new_dashboard_with_geomap_widget",
    description=None,
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=30,
            ),
            definition=GeomapWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                time=WidgetTime(),
                type=GeomapWidgetDefinitionType.GEOMAP,
                requests=[
                    GeomapWidgetRequest(
                        formulas=[
                            WidgetFormula(
                                formula="query1",
                                limit=WidgetFormulaLimit(
                                    count=250,
                                    order=QuerySortOrder.DESC,
                                ),
                            ),
                        ],
                        queries=[
                            FormulaAndFunctionEventQueryDefinition(
                                name="query1",
                                data_source=FormulaAndFunctionEventsDataSource.RUM,
                                search=FormulaAndFunctionEventQueryDefinitionSearch(
                                    query="",
                                ),
                                indexes=[
                                    "*",
                                ],
                                compute=FormulaAndFunctionEventQueryDefinitionCompute(
                                    aggregation=FormulaAndFunctionEventAggregation.COUNT,
                                ),
                                group_by=[
                                    FormulaAndFunctionEventQueryGroupBy(
                                        facet="@geo.country_iso_code",
                                        limit=250,
                                        sort=FormulaAndFunctionEventQueryGroupBySort(
                                            order=QuerySortOrder.DESC,
                                            aggregation=FormulaAndFunctionEventAggregation.COUNT,
                                        ),
                                    ),
                                ],
                            ),
                        ],
                        response_format=FormulaAndFunctionResponseFormat.SCALAR,
                    ),
                ],
                style=GeomapWidgetDefinitionStyle(
                    palette="hostmap_blues",
                    palette_flip=False,
                ),
                view=GeomapWidgetDefinitionView(
                    focus="WORLD",
                ),
            ),
        ),
    ],
    template_variables=[],
    layout_type=DashboardLayoutType.FREE,
    is_read_only=False,
    notify_list=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
