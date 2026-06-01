"""
Patch an incident impact returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_impact_create_attributes import IncidentImpactCreateAttributes
from datadog_api_client.v2.model.incident_impact_create_data import IncidentImpactCreateData
from datadog_api_client.v2.model.incident_impact_create_request import IncidentImpactCreateRequest
from datadog_api_client.v2.model.incident_impact_fields_object import IncidentImpactFieldsObject
from datadog_api_client.v2.model.incident_impact_type import IncidentImpactType
from datetime import datetime
from dateutil.tz import tzutc

body = IncidentImpactCreateRequest(
    data=IncidentImpactCreateData(
        attributes=IncidentImpactCreateAttributes(
            description="Service was unavailable for external users",
            end_at=datetime(2025, 8, 29, 13, 17, tzinfo=tzutc()),
            fields=IncidentImpactFieldsObject(
                [("customers_impacted", "all"), ("products_impacted", "['shopping', 'marketing']")]
            ),
            start_at=datetime(2025, 8, 28, 13, 17, tzinfo=tzutc()),
        ),
        type=IncidentImpactType.INCIDENT_IMPACTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["patch_incident_impact"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.patch_incident_impact(incident_id="incident_id", impact_id="impact_id", body=body)

    print(response)
