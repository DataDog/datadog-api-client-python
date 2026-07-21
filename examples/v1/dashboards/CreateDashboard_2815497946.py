"""
Create a new dashboard with topology_map data_streams widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.topology_map_widget_definition_data_streams import (
    TopologyMapWidgetDefinitionDataStreams,
)
from datadog_api_client.v1.model.topology_map_widget_definition_type import TopologyMapWidgetDefinitionType
from datadog_api_client.v1.model.topology_query_data_streams import TopologyQueryDataStreams
from datadog_api_client.v1.model.topology_query_data_streams_data_source import TopologyQueryDataStreamsDataSource
from datadog_api_client.v1.model.topology_request_data_streams import TopologyRequestDataStreams
from datadog_api_client.v1.model.topology_request_type import TopologyRequestType
from datadog_api_client.v1.model.widget import Widget
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
            definition=TopologyMapWidgetDefinitionDataStreams(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=TopologyMapWidgetDefinitionType.TOPOLOGY_MAP,
                requests=[
                    TopologyRequestDataStreams(
                        request_type=TopologyRequestType.TOPOLOGY,
                        query=TopologyQueryDataStreams(
                            data_source=TopologyQueryDataStreamsDataSource.DATA_STREAMS,
                            service="",
                            filters=[
                                "env:prod",
                            ],
                            query_string="service:myservice",
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
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)
