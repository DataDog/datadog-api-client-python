"""
Create App returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.app_definition_type import AppDefinitionType
from datadog_api_client.v2.model.component import Component
from datadog_api_client.v2.model.component_grid import ComponentGrid
from datadog_api_client.v2.model.component_grid_properties import ComponentGridProperties
from datadog_api_client.v2.model.component_grid_type import ComponentGridType
from datadog_api_client.v2.model.component_properties import ComponentProperties
from datadog_api_client.v2.model.component_type import ComponentType
from datadog_api_client.v2.model.create_app_request import CreateAppRequest
from datadog_api_client.v2.model.create_app_request_data import CreateAppRequestData
from datadog_api_client.v2.model.create_app_request_data_attributes import CreateAppRequestDataAttributes

body = CreateAppRequest(
    data=CreateAppRequestData(
        attributes=CreateAppRequestDataAttributes(
            components=[
                ComponentGrid(
                    events=[],
                    name="grid0",
                    properties=ComponentGridProperties(
                        children=[
                            Component(
                                events=[],
                                name="gridCell0",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            events=[],
                                            name="calloutValue0",
                                            properties=ComponentProperties(
                                                is_visible=True,
                                                is_unpublishd=False,
                                                is_loading=False,
                                                label="CPU Usage",
                                                size="sm",
                                                style="vivid_yellow",
                                                unit="kB",
                                                value="42",
                                            ),
                                            type=ComponentType.CALLOUTVALUE,
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'height': 8, 'width': 2, 'x': 0, 'y': 0}")]),
                                ),
                                type=ComponentType.GRIDCELL,
                            ),
                        ],
                    ),
                    type=ComponentGridType.GRID,
                ),
            ],
            description="This is a simple example app",
            queries=[],
            name="Example App",
            root_instance_name="grid0",
        ),
        type=AppDefinitionType.APPDEFINITIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_app"] = True
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.create_app(body=body)

    print(response)
