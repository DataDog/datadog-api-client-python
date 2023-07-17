"""
Create a geomap widget using an event_list request
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.dashboard_reflow_type import DashboardReflowType
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.geomap_widget_definition import GeomapWidgetDefinition
from datadog_api_client.v1.model.geomap_widget_definition_style import GeomapWidgetDefinitionStyle
from datadog_api_client.v1.model.geomap_widget_definition_type import GeomapWidgetDefinitionType
from datadog_api_client.v1.model.geomap_widget_definition_view import GeomapWidgetDefinitionView
from datadog_api_client.v1.model.geomap_widget_request import GeomapWidgetRequest
from datadog_api_client.v1.model.list_stream_column import ListStreamColumn
from datadog_api_client.v1.model.list_stream_column_width import ListStreamColumnWidth
from datadog_api_client.v1.model.list_stream_query import ListStreamQuery
from datadog_api_client.v1.model.list_stream_source import ListStreamSource
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    description="Example-Dashboard",
    widgets=[
        Widget(
            definition=GeomapWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=GeomapWidgetDefinitionType.GEOMAP,
                requests=[
                    GeomapWidgetRequest(
                        response_format=FormulaAndFunctionResponseFormat.EVENT_LIST,
                        query=ListStreamQuery(
                            data_source=ListStreamSource.LOGS_STREAM,
                            query_string="",
                            indexes=[],
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
                            ListStreamColumn(
                                field="classic",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                            ListStreamColumn(
                                field="",
                                width=ListStreamColumnWidth.AUTO,
                            ),
                        ],
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
