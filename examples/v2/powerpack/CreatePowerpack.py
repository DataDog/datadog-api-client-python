"""
Create a new powerpack returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.powerpack_api import PowerpackApi
from datadog_api_client.v2.model.powerpack import Powerpack
from datadog_api_client.v2.model.powerpack_attributes import PowerpackAttributes
from datadog_api_client.v2.model.powerpack_data import PowerpackData
from datadog_api_client.v2.model.powerpack_group_widget import PowerpackGroupWidget
from datadog_api_client.v2.model.powerpack_group_widget_definition import PowerpackGroupWidgetDefinition
from datadog_api_client.v2.model.powerpack_group_widget_layout import PowerpackGroupWidgetLayout
from datadog_api_client.v2.model.powerpack_inner_widgets import PowerpackInnerWidgets
from datadog_api_client.v2.model.powerpack_template_variable import PowerpackTemplateVariable
from datadog_api_client.v2.model.widget_live_span import WidgetLiveSpan

body = Powerpack(
    data=PowerpackData(
        attributes=PowerpackAttributes(
            description="Sample powerpack",
            group_widget=PowerpackGroupWidget(
                definition=PowerpackGroupWidgetDefinition(
                    layout_type="ordered",
                    show_title=True,
                    title="Sample Powerpack",
                    type="group",
                    widgets=[
                        PowerpackInnerWidgets(
                            definition=dict([("content", "test"), ("type", "note")]),
                        ),
                    ],
                ),
                layout=PowerpackGroupWidgetLayout(
                    height=3,
                    width=12,
                    x=0,
                    y=0,
                ),
                live_span=WidgetLiveSpan.PAST_ONE_HOUR,
            ),
            name="Example-Powerpack",
            tags=[
                "tag:sample",
            ],
            template_variables=[
                PowerpackTemplateVariable(
                    defaults=[
                        "*",
                    ],
                    name="sample",
                ),
            ],
        ),
        type="powerpack",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PowerpackApi(api_client)
    response = api_instance.create_powerpack(body=body)

    print(response)
