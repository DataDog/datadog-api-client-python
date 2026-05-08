"""
Create a new dashboard with point_plot widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.data_projection_query import DataProjectionQuery
from datadog_api_client.v1.model.data_projection_request_type import DataProjectionRequestType
from datadog_api_client.v1.model.point_plot_dimension import PointPlotDimension
from datadog_api_client.v1.model.point_plot_projection import PointPlotProjection
from datadog_api_client.v1.model.point_plot_projection_dimension import PointPlotProjectionDimension
from datadog_api_client.v1.model.point_plot_projection_type import PointPlotProjectionType
from datadog_api_client.v1.model.point_plot_widget_definition import PointPlotWidgetDefinition
from datadog_api_client.v1.model.point_plot_widget_definition_type import PointPlotWidgetDefinitionType
from datadog_api_client.v1.model.point_plot_widget_request import PointPlotWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    layout_type=DashboardLayoutType.ORDERED,
    widgets=[
        Widget(
            definition=PointPlotWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=PointPlotWidgetDefinitionType.POINT_PLOT,
                requests=[
                    PointPlotWidgetRequest(
                        request_type=DataProjectionRequestType.DATA_PROJECTION,
                        query=DataProjectionQuery(
                            query_string="service:web-store",
                            data_source="logs",
                        ),
                        projection=PointPlotProjection(
                            type=PointPlotProjectionType.POINT_PLOT,
                            dimensions=[
                                PointPlotProjectionDimension(
                                    column="host",
                                    dimension=PointPlotDimension.GROUP,
                                ),
                                PointPlotProjectionDimension(
                                    column="@duration",
                                    dimension=PointPlotDimension.Y,
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
