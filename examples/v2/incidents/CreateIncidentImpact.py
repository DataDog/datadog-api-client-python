"""
Create an incident impact returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_impact_create_attributes import IncidentImpactCreateAttributes
from datadog_api_client.v2.model.incident_impact_create_data import IncidentImpactCreateData
from datadog_api_client.v2.model.incident_impact_create_request import IncidentImpactCreateRequest
from datadog_api_client.v2.model.incident_impact_type import IncidentImpactType
from datetime import datetime
from dateutil.tz import tzutc

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentImpactCreateRequest(
    data=IncidentImpactCreateData(
        type=IncidentImpactType.INCIDENT_IMPACTS,
        attributes=IncidentImpactCreateAttributes(
            start_at=datetime(2025, 9, 12, 13, 50, tzinfo=tzutc()),
            end_at=datetime(2025, 9, 12, 14, 50, tzinfo=tzutc()),
            description="Outage in the us-east-1 region",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_impact"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_impact(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)
