"""
Create an incident user-defined role returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_user_defined_role_data_attributes_request import (
    IncidentUserDefinedRoleDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_user_defined_role_data_request import IncidentUserDefinedRoleDataRequest
from datadog_api_client.v2.model.incident_user_defined_role_incident_type_relationship import (
    IncidentUserDefinedRoleIncidentTypeRelationship,
)
from datadog_api_client.v2.model.incident_user_defined_role_incident_type_relationship_data import (
    IncidentUserDefinedRoleIncidentTypeRelationshipData,
)
from datadog_api_client.v2.model.incident_user_defined_role_policy import IncidentUserDefinedRolePolicy
from datadog_api_client.v2.model.incident_user_defined_role_relationships_request import (
    IncidentUserDefinedRoleRelationshipsRequest,
)
from datadog_api_client.v2.model.incident_user_defined_role_request import IncidentUserDefinedRoleRequest
from datadog_api_client.v2.model.incident_user_defined_role_type import IncidentUserDefinedRoleType
from uuid import UUID

body = IncidentUserDefinedRoleRequest(
    data=IncidentUserDefinedRoleDataRequest(
        attributes=IncidentUserDefinedRoleDataAttributesRequest(
            description="The technical lead for the incident.",
            name="Tech Lead",
            policy=IncidentUserDefinedRolePolicy(
                is_single=True,
            ),
        ),
        relationships=IncidentUserDefinedRoleRelationshipsRequest(
            incident_type=IncidentUserDefinedRoleIncidentTypeRelationship(
                data=IncidentUserDefinedRoleIncidentTypeRelationshipData(
                    id=UUID("00000000-0000-0000-0000-000000000001"),
                    type="incident_types",
                ),
            ),
        ),
        type=IncidentUserDefinedRoleType.INCIDENT_USER_DEFINED_ROLES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_user_defined_role"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_user_defined_role(body=body)

    print(response)
