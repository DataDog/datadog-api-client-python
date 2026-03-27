"""
Delete a widget returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.widgets_api import WidgetsApi
from datadog_api_client.v2.model.widget_experience_type import WidgetExperienceType
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WidgetsApi(api_client)
    api_instance.delete_widget(
        experience_type=WidgetExperienceType.CCM_REPORTS,
        uuid=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )
