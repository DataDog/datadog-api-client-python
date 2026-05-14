"""
Create an incident role assignment returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_role_assignment_data_attributes_request import (
    IncidentRoleAssignmentDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_role_assignment_data_request import IncidentRoleAssignmentDataRequest
from datadog_api_client.v2.model.incident_role_assignment_relationships_request import (
    IncidentRoleAssignmentRelationshipsRequest,
)
from datadog_api_client.v2.model.incident_role_assignment_request import IncidentRoleAssignmentRequest
from datadog_api_client.v2.model.incident_role_assignment_responder_relationship import (
    IncidentRoleAssignmentResponderRelationship,
)
from datadog_api_client.v2.model.incident_role_assignment_responder_relationship_data import (
    IncidentRoleAssignmentResponderRelationshipData,
)
from datadog_api_client.v2.model.incident_role_assignment_role_relationship import (
    IncidentRoleAssignmentRoleRelationship,
)
from datadog_api_client.v2.model.incident_role_assignment_role_relationship_data import (
    IncidentRoleAssignmentRoleRelationshipData,
)
from datadog_api_client.v2.model.incident_role_assignment_type import IncidentRoleAssignmentType
from uuid import UUID

body = IncidentRoleAssignmentRequest(
    data=IncidentRoleAssignmentDataRequest(
        attributes=IncidentRoleAssignmentDataAttributesRequest(
            role="commander",
        ),
        relationships=IncidentRoleAssignmentRelationshipsRequest(
            reserved_role=IncidentRoleAssignmentRoleRelationship(
                data=IncidentRoleAssignmentRoleRelationshipData(
                    id=UUID("00000000-0000-0000-0000-000000000000"),
                    type="incident_reserved_roles",
                ),
            ),
            responder=IncidentRoleAssignmentResponderRelationship(
                data=IncidentRoleAssignmentResponderRelationshipData(
                    id=UUID("00000000-0000-0000-0000-000000000000"),
                    type="users",
                ),
            ),
            user_defined_role=IncidentRoleAssignmentRoleRelationship(
                data=IncidentRoleAssignmentRoleRelationshipData(
                    id=UUID("00000000-0000-0000-0000-000000000000"),
                    type="incident_reserved_roles",
                ),
            ),
        ),
        type=IncidentRoleAssignmentType.INCIDENT_ROLE_ASSIGNMENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_role_assignment"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_role_assignment(body=body)

    print(response)
