"""
Update global incident settings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.global_incident_settings_attributes_request import (
    GlobalIncidentSettingsAttributesRequest,
)
from datadog_api_client.v2.model.global_incident_settings_data_request import GlobalIncidentSettingsDataRequest
from datadog_api_client.v2.model.global_incident_settings_request import GlobalIncidentSettingsRequest
from datadog_api_client.v2.model.global_incident_settings_type import GlobalIncidentSettingsType

body = GlobalIncidentSettingsRequest(
    data=GlobalIncidentSettingsDataRequest(
        attributes=GlobalIncidentSettingsAttributesRequest(
            analytics_dashboard_id="abc-123-def",
        ),
        type=GlobalIncidentSettingsType.INCIDENTS_GLOBAL_SETTINGS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_global_incident_settings"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_global_incident_settings(body=body)

    print(response)
