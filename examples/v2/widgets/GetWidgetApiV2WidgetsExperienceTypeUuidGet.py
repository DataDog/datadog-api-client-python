"""
Get a widget returns "Successful Response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.widgets_api import WidgetsApi
from datadog_api_client.v2.model.widget_experience_type import WidgetExperienceType
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WidgetsApi(api_client)
    response = api_instance.get_widget_api_v2_widgets_experience_type_uuid_get(
        uuid=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        experience_type=WidgetExperienceType.CCM_REPORTS,
    )

    print(response)
