"""
Update an incident type returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_type_patch_data import IncidentTypePatchData
from datadog_api_client.v2.model.incident_type_patch_request import IncidentTypePatchRequest
from datadog_api_client.v2.model.incident_type_type import IncidentTypeType
from datadog_api_client.v2.model.incident_type_update_attributes import IncidentTypeUpdateAttributes

body = IncidentTypePatchRequest(
    data=IncidentTypePatchData(
        attributes=IncidentTypeUpdateAttributes(
            description="Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data. Note: This will notify the security team.",
            is_default=True,
            name="Security Incident",
        ),
        type=IncidentTypeType.INCIDENT_TYPES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_type"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_type(incident_type_id="incident_type_id", body=body)

    print(response)
