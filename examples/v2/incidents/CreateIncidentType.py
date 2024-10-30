"""
Create an incident type returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_type_attributes import IncidentTypeAttributes
from datadog_api_client.v2.model.incident_type_create_data import IncidentTypeCreateData
from datadog_api_client.v2.model.incident_type_create_request import IncidentTypeCreateRequest
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType

body = IncidentTypeCreateRequest(
    data=IncidentTypeCreateData(
        attributes=IncidentTypeAttributes(
            description="8d4bbb66dccf2456",
            is_default=True,
            name="8d4bbb66dccf2456",
        ),
        type=IncidentTypeType.INCIDENT_TYPES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_type"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_type(body=body)

    print(response)