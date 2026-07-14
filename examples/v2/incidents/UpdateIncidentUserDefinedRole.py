"""
Update an incident user-defined role returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_user_defined_role_patch_data_attributes_request import (
    IncidentUserDefinedRolePatchDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_user_defined_role_patch_data_request import (
    IncidentUserDefinedRolePatchDataRequest,
)
from datadog_api_client.v2.model.incident_user_defined_role_patch_request import IncidentUserDefinedRolePatchRequest
from datadog_api_client.v2.model.incident_user_defined_role_policy import IncidentUserDefinedRolePolicy
from datadog_api_client.v2.model.incident_user_defined_role_type import IncidentUserDefinedRoleType
from uuid import UUID

body = IncidentUserDefinedRolePatchRequest(
    data=IncidentUserDefinedRolePatchDataRequest(
        attributes=IncidentUserDefinedRolePatchDataAttributesRequest(
            description="The technical lead for the incident.",
            name="Tech Lead",
            policy=IncidentUserDefinedRolePolicy(
                is_single=True,
            ),
        ),
        id=UUID("00000000-0000-0000-0000-000000000002"),
        type=IncidentUserDefinedRoleType.INCIDENT_USER_DEFINED_ROLES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_user_defined_role"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_user_defined_role(
        role_id=UUID("00000000-0000-0000-0000-000000000002"), body=body
    )

    print(response)
