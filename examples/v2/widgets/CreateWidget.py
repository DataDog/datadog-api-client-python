"""
Create a widget returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.widgets_api import WidgetsApi
from datadog_api_client.v2.model.create_or_update_widget_request import CreateOrUpdateWidgetRequest
from datadog_api_client.v2.model.create_or_update_widget_request_attributes import CreateOrUpdateWidgetRequestAttributes
from datadog_api_client.v2.model.create_or_update_widget_request_data import CreateOrUpdateWidgetRequestData
from datadog_api_client.v2.model.widget_definition import WidgetDefinition
from datadog_api_client.v2.model.widget_experience_type import WidgetExperienceType
from datadog_api_client.v2.model.widget_type import WidgetType

body = CreateOrUpdateWidgetRequest(
    data=CreateOrUpdateWidgetRequestData(
        attributes=CreateOrUpdateWidgetRequestAttributes(
            definition=WidgetDefinition(
                title="My Widget",
                type=WidgetType.BAR_CHART,
            ),
            tags=[],
        ),
        type="widgets",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WidgetsApi(api_client)
    response = api_instance.create_widget(experience_type=WidgetExperienceType.CCM_REPORTS, body=body)

    print(response)
