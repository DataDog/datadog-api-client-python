"""
Create an incident integration metadata returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_integration_metadata_attributes import IncidentIntegrationMetadataAttributes
from datadog_api_client.v2.model.incident_integration_metadata_create_data import IncidentIntegrationMetadataCreateData
from datadog_api_client.v2.model.incident_integration_metadata_create_request import (
    IncidentIntegrationMetadataCreateRequest,
)
from datadog_api_client.v2.model.incident_integration_metadata_type import IncidentIntegrationMetadataType
from datadog_api_client.v2.model.slack_integration_metadata import SlackIntegrationMetadata
from datadog_api_client.v2.model.slack_integration_metadata_channel_item import SlackIntegrationMetadataChannelItem

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentIntegrationMetadataCreateRequest(
    data=IncidentIntegrationMetadataCreateData(
        attributes=IncidentIntegrationMetadataAttributes(
            incident_id=INCIDENT_DATA_ID,
            integration_type=1,
            metadata=SlackIntegrationMetadata(
                channels=[
                    SlackIntegrationMetadataChannelItem(
                        channel_id="C0123456789",
                        channel_name="#new-channel",
                        team_id="T01234567",
                        redirect_url="https://slack.com/app_redirect?channel=C0123456789&team=T01234567",
                    ),
                ],
            ),
        ),
        type=IncidentIntegrationMetadataType.INCIDENT_INTEGRATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_integration"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_integration(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)
