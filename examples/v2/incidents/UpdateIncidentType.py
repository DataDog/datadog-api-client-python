"""
Update an incident type returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_type_patch_data import IncidentTypePatchData
from datadog_api_client.v2.model.incident_type_patch_request import IncidentTypePatchRequest
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType
from datadog_api_client.v2.model.incident_type_update_attributes import IncidentTypeUpdateAttributes

# there is a valid "incident_type" in the system
INCIDENT_TYPE_DATA_ATTRIBUTES_NAME = environ["INCIDENT_TYPE_DATA_ATTRIBUTES_NAME"]
INCIDENT_TYPE_DATA_ID = environ["INCIDENT_TYPE_DATA_ID"]

body = IncidentTypePatchRequest(
    data=IncidentTypePatchData(
        id=INCIDENT_TYPE_DATA_ID,
        attributes=IncidentTypeUpdateAttributes(
            name="Security Incident-updated",
        ),
        type=IncidentTypeType.INCIDENT_TYPES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_type"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_type(incident_type_id=INCIDENT_TYPE_DATA_ID, body=body)

    print(response)
