"""
Create a new dashboard with hostmap DDSQL widget
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.dataset_list_query import DatasetListQuery
from datadog_api_client.v1.model.dataset_list_query_data_source_type import DatasetListQueryDataSourceType
from datadog_api_client.v1.model.host_map_widget_definition import HostMapWidgetDefinition
from datadog_api_client.v1.model.host_map_widget_definition_request_type import HostMapWidgetDefinitionRequestType
from datadog_api_client.v1.model.host_map_widget_definition_requests import HostMapWidgetDefinitionRequests
from datadog_api_client.v1.model.host_map_widget_definition_type import HostMapWidgetDefinitionType
from datadog_api_client.v1.model.host_map_widget_dimension import HostMapWidgetDimension
from datadog_api_client.v1.model.host_map_widget_infrastructure_style import HostMapWidgetInfrastructureStyle
from datadog_api_client.v1.model.host_map_widget_projection import HostMapWidgetProjection
from datadog_api_client.v1.model.host_map_widget_projection_dimension_mapping import (
    HostMapWidgetProjectionDimensionMapping,
)
from datadog_api_client.v1.model.host_map_widget_projection_type import HostMapWidgetProjectionType
from datadog_api_client.v1.model.published_dataset_provider import PublishedDatasetProvider
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout import WidgetLayout
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

body = Dashboard(
    title="Example-Dashboard",
    description=None,
    widgets=[
        Widget(
            layout=WidgetLayout(
                x=0,
                y=0,
                width=47,
                height=22,
            ),
            definition=HostMapWidgetDefinition(
                title="",
                title_size="16",
                title_align=WidgetTextAlign.LEFT,
                type=HostMapWidgetDefinitionType.HOSTMAP,
                requests=HostMapWidgetDefinitionRequests(
                    request_type=HostMapWidgetDefinitionRequestType.DATA_PROJECTION,
                    limit=1000,
                    query=DatasetListQuery(
                        data_source=DatasetListQueryDataSourceType.DATASET,
                        dataset_provider=PublishedDatasetProvider.DDSQL_QUERY,
                        dataset_id="abc-123-def",
                    ),
                    projection=HostMapWidgetProjection(
                        type=HostMapWidgetProjectionType.HOSTMAP,
                        dimensions=[
                            HostMapWidgetProjectionDimensionMapping(
                                column="entity_id",
                                dimension=HostMapWidgetDimension.NODE,
                            ),
                            HostMapWidgetProjectionDimensionMapping(
                                column="parent_id",
                                dimension=HostMapWidgetDimension.GROUP,
                            ),
                            HostMapWidgetProjectionDimensionMapping(
                                column="cpu_usage",
                                dimension=HostMapWidgetDimension.FILL,
                            ),
                        ],
                    ),
                    style=HostMapWidgetInfrastructureStyle(
                        palette="green_to_orange",
                        palette_flip=False,
                    ),
                ),
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
