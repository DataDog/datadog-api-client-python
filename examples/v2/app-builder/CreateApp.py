"""
Create App returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.action_query import ActionQuery
from datadog_api_client.v2.model.action_query_properties import ActionQueryProperties
from datadog_api_client.v2.model.action_query_spec_input import ActionQuerySpecInput
from datadog_api_client.v2.model.action_query_spec_object import ActionQuerySpecObject
from datadog_api_client.v2.model.action_query_type import ActionQueryType
from datadog_api_client.v2.model.app_builder_event import AppBuilderEvent
from datadog_api_client.v2.model.app_builder_event_name import AppBuilderEventName
from datadog_api_client.v2.model.app_builder_event_type import AppBuilderEventType
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
from datadog_api_client.v2.model.data_transform import DataTransform
from datadog_api_client.v2.model.data_transform_properties import DataTransformProperties
from datadog_api_client.v2.model.data_transform_type import DataTransformType
from datadog_api_client.v2.model.state_variable import StateVariable
from datadog_api_client.v2.model.state_variable_properties import StateVariableProperties
from datadog_api_client.v2.model.state_variable_type import StateVariableType
from uuid import UUID

body = CreateAppRequest(
    data=CreateAppRequestData(
        type=AppDefinitionType.APPDEFINITIONS,
        attributes=CreateAppRequestDataAttributes(
            root_instance_name="grid0",
            components=[
                ComponentGrid(
                    name="grid0",
                    type=ComponentGridType.GRID,
                    properties=ComponentGridProperties(
                        children=[
                            Component(
                                type=ComponentType.GRIDCELL,
                                name="gridCell0",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            name="text0",
                                            type=ComponentType.TEXT,
                                            properties=ComponentProperties(
                                                content="# Cat Facts",
                                                content_type="markdown",
                                                text_align="left",
                                                vertical_align="top",
                                                is_visible=True,
                                            ),
                                            events=[],
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'x': 0, 'y': 0, 'width': 4, 'height': 5}")]),
                                ),
                                events=[],
                            ),
                            Component(
                                type=ComponentType.GRIDCELL,
                                name="gridCell2",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            name="table0",
                                            type=ComponentType.TABLE,
                                            properties=ComponentProperties(
                                                data="${fetchFacts?.outputs?.body?.data}",
                                                columns=[
                                                    dict(
                                                        [
                                                            ("dataPath", "fact"),
                                                            ("header", "fact"),
                                                            ("isHidden", "False"),
                                                            ("id", "0ae2ae9e-0280-4389-83c6-1c5949f7e674"),
                                                        ]
                                                    ),
                                                    dict(
                                                        [
                                                            ("dataPath", "length"),
                                                            ("header", "length"),
                                                            ("isHidden", "True"),
                                                            ("id", "c9048611-0196-4a00-9366-1ef9e3ec0408"),
                                                        ]
                                                    ),
                                                    dict(
                                                        [
                                                            ("id", "8fa9284b-7a58-4f13-9959-57b7d8a7fe8f"),
                                                            ("dataPath", "Due Date"),
                                                            ("header", "Unused Old Column"),
                                                            ("disableSortBy", "False"),
                                                            (
                                                                "formatter",
                                                                "{'type': 'formatted_time', 'format': 'LARGE_WITHOUT_TIME'}",
                                                            ),
                                                            ("isDeleted", "True"),
                                                        ]
                                                    ),
                                                ],
                                                summary=True,
                                                page_size="${pageSize?.value}",
                                                pagination_type="server_side",
                                                is_loading="${fetchFacts?.isLoading}",
                                                row_buttons=[],
                                                is_wrappable=False,
                                                is_scrollable="vertical",
                                                is_sub_rows_enabled=False,
                                                global_filter=False,
                                                is_visible=True,
                                                total_count="${fetchFacts?.outputs?.body?.total}",
                                            ),
                                            events=[],
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'x': 0, 'y': 5, 'width': 12, 'height': 96}")]),
                                ),
                                events=[],
                            ),
                            Component(
                                type=ComponentType.GRIDCELL,
                                name="gridCell1",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            name="text1",
                                            type=ComponentType.TEXT,
                                            properties=ComponentProperties(
                                                content="## Random Fact\n\n${randomFact?.outputs?.fact}",
                                                content_type="markdown",
                                                text_align="left",
                                                vertical_align="top",
                                                is_visible=True,
                                            ),
                                            events=[],
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'x': 0, 'y': 101, 'width': 12, 'height': 16}")]),
                                ),
                                events=[],
                            ),
                            Component(
                                type=ComponentType.GRIDCELL,
                                name="gridCell3",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            name="button0",
                                            type=ComponentType.BUTTON,
                                            properties=ComponentProperties(
                                                label="Increase Page Size",
                                                level="default",
                                                is_primary=True,
                                                is_borderless=False,
                                                is_loading=False,
                                                is_disabled=False,
                                                is_visible=True,
                                                icon_left="angleUp",
                                                icon_right="",
                                            ),
                                            events=[
                                                AppBuilderEvent(
                                                    variable_name="pageSize",
                                                    value="${pageSize?.value + 1}",
                                                    name=AppBuilderEventName.CLICK,
                                                    type=AppBuilderEventType.SETSTATEVARIABLEVALUE,
                                                ),
                                            ],
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'x': 10, 'y': 134, 'width': 2, 'height': 4}")]),
                                ),
                                events=[],
                            ),
                            Component(
                                type=ComponentType.GRIDCELL,
                                name="gridCell4",
                                properties=ComponentProperties(
                                    children=[
                                        Component(
                                            name="button1",
                                            type=ComponentType.BUTTON,
                                            properties=ComponentProperties(
                                                label="Decrease Page Size",
                                                level="default",
                                                is_primary=True,
                                                is_borderless=False,
                                                is_loading=False,
                                                is_disabled=False,
                                                is_visible=True,
                                                icon_left="angleDown",
                                                icon_right="",
                                            ),
                                            events=[
                                                AppBuilderEvent(
                                                    variable_name="pageSize",
                                                    value="${pageSize?.value - 1}",
                                                    name=AppBuilderEventName.CLICK,
                                                    type=AppBuilderEventType.SETSTATEVARIABLEVALUE,
                                                ),
                                            ],
                                        ),
                                    ],
                                    is_visible="true",
                                    layout=dict([("default", "{'x': 10, 'y': 138, 'width': 2, 'height': 4}")]),
                                ),
                                events=[],
                            ),
                        ],
                        background_color="default",
                    ),
                    events=[],
                ),
            ],
            queries=[
                ActionQuery(
                    id=UUID("92ff0bb8-553b-4f31-87c7-ef5bd16d47d5"),
                    type=ActionQueryType.ACTION,
                    name="fetchFacts",
                    events=[],
                    properties=ActionQueryProperties(
                        spec=ActionQuerySpecObject(
                            fqn="com.datadoghq.http.request",
                            connection_id="5e63f4a8-4ce6-47de-ba11-f6617c1d54f3",
                            inputs=ActionQuerySpecInput(
                                [
                                    ("verb", "GET"),
                                    ("url", "https://catfact.ninja/facts"),
                                    (
                                        "urlParams",
                                        "[{'key': 'limit', 'value': '${pageSize.value.toString()}'}, {'key': 'page', 'value': '${(table0.pageIndex + 1).toString()}'}]",
                                    ),
                                ]
                            ),
                        ),
                    ),
                ),
                StateVariable(
                    type=StateVariableType.STATEVARIABLE,
                    name="pageSize",
                    properties=StateVariableProperties(
                        default_value="${20}",
                    ),
                    id=UUID("afd03c81-4075-4432-8618-ba09d52d2f2d"),
                ),
                DataTransform(
                    type=DataTransformType.DATATRANSFORM,
                    name="randomFact",
                    properties=DataTransformProperties(
                        outputs="${(() => {const facts = fetchFacts.outputs.body.data\nreturn facts[Math.floor(Math.random()*facts.length)]\n})()}",
                    ),
                    id=UUID("0fb22859-47dc-4137-9e41-7b67d04c525c"),
                ),
            ],
            name="Example Cat Facts Viewer",
            description="This is a slightly complicated example app that fetches and displays cat facts",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.create_app(body=body)

    print(response)
