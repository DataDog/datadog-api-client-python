"""
Search widgets returns "Successful Response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.widgets_api import WidgetsApi
from datadog_api_client.v2.model.widget_experience_type import WidgetExperienceType

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WidgetsApi(api_client)
    response = api_instance.search_widgets_api_v2_widgets_experience_type_get(
        experience_type=WidgetExperienceType.CCM_REPORTS,
    )

    print(response)
