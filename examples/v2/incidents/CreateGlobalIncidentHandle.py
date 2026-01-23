"""
Create global incident handle returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_handle_attributes_fields import IncidentHandleAttributesFields
from datadog_api_client.v2.model.incident_handle_attributes_request import IncidentHandleAttributesRequest
from datadog_api_client.v2.model.incident_handle_data_request import IncidentHandleDataRequest
from datadog_api_client.v2.model.incident_handle_relationship import IncidentHandleRelationship
from datadog_api_client.v2.model.incident_handle_relationship_data import IncidentHandleRelationshipData
from datadog_api_client.v2.model.incident_handle_relationships_request import IncidentHandleRelationshipsRequest
from datadog_api_client.v2.model.incident_handle_request import IncidentHandleRequest
from datadog_api_client.v2.model.incident_handle_type import IncidentHandleType

body = IncidentHandleRequest(
    data=IncidentHandleDataRequest(
        attributes=IncidentHandleAttributesRequest(
            fields=IncidentHandleAttributesFields(
                severity=[
                    "SEV-1",
                ],
            ),
            name="@incident-sev-1",
        ),
        id="b2494081-cdf0-4205-b366-4e1dd4fdf0bf",
        relationships=IncidentHandleRelationshipsRequest(
            commander_user=IncidentHandleRelationship(
                data=IncidentHandleRelationshipData(
                    id="f7b538b1-ed7c-4e84-82de-fdf84a539d40",
                    type="incident_types",
                ),
            ),
            incident_type=IncidentHandleRelationship(
                data=IncidentHandleRelationshipData(
                    id="f7b538b1-ed7c-4e84-82de-fdf84a539d40",
                    type="incident_types",
                ),
            ),
        ),
        type=IncidentHandleType.INCIDENTS_HANDLES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_global_incident_handle"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_global_incident_handle(body=body)

    print(response)
