"""
Link incident to case returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.incident_relationship_data import IncidentRelationshipData
from datadog_api_client.v2.model.incident_resource_type import IncidentResourceType
from datadog_api_client.v2.model.relationship_to_incident_request import RelationshipToIncidentRequest

body = RelationshipToIncidentRequest(
    data=IncidentRelationshipData(
        id="00000000-0000-0000-0000-000000000000",
        type=IncidentResourceType.INCIDENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["link_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.link_incident(case_id="case_id", body=body)

    print(response)
