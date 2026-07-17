"""
Create a new dashboard with a live default_timeframe returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.dashboard_live_timeframe import DashboardLiveTimeframe
from datadog_api_client.v1.model.dashboard_live_timeframe_type import DashboardLiveTimeframeType
from datadog_api_client.v1.model.note_widget_definition import NoteWidgetDefinition
from datadog_api_client.v1.model.note_widget_definition_type import NoteWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_live_span_unit import WidgetLiveSpanUnit
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_tick_edge import WidgetTickEdge

body = Dashboard(
    title="Example-Dashboard",
    layout_type=DashboardLayoutType.ORDERED,
    widgets=[
        Widget(
            definition=NoteWidgetDefinition(
                type=NoteWidgetDefinitionType.NOTE,
                content="test",
                background_color="white",
                font_size="14",
                text_align=WidgetTextAlign.LEFT,
                show_tick=False,
                tick_pos="50%",
                tick_edge=WidgetTickEdge.LEFT,
            ),
        ),
    ],
    default_timeframe=DashboardLiveTimeframe(
        type=DashboardLiveTimeframeType.LIVE,
        unit=WidgetLiveSpanUnit.HOUR,
        value=4,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
