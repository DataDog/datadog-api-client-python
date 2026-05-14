"""
Create an incident Microsoft Teams configuration returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_microsoft_teams_configuration_data_attributes_request import (
    IncidentMicrosoftTeamsConfigurationDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_microsoft_teams_configuration_data_request import (
    IncidentMicrosoftTeamsConfigurationDataRequest,
)
from datadog_api_client.v2.model.incident_microsoft_teams_configuration_request import (
    IncidentMicrosoftTeamsConfigurationRequest,
)
from datadog_api_client.v2.model.incident_microsoft_teams_configuration_type import (
    IncidentMicrosoftTeamsConfigurationType,
)

body = IncidentMicrosoftTeamsConfigurationRequest(
    data=IncidentMicrosoftTeamsConfigurationDataRequest(
        attributes=IncidentMicrosoftTeamsConfigurationDataAttributesRequest(
            manual_meeting_creation=False,
            post_meeting_summary=True,
        ),
        type=IncidentMicrosoftTeamsConfigurationType.MICROSOFT_TEAMS_CONFIGURATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_microsoft_teams_configuration"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_microsoft_teams_configuration(body=body)

    print(response)
