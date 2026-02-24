"""
Import an incident returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_import_request import IncidentImportRequest
from datadog_api_client.v2.model.incident_import_request_attributes import IncidentImportRequestAttributes
from datadog_api_client.v2.model.incident_import_request_data import IncidentImportRequestData
from datadog_api_client.v2.model.incident_import_visibility import IncidentImportVisibility
from datadog_api_client.v2.model.incident_type import IncidentType

body = IncidentImportRequest(
    data=IncidentImportRequestData(
        type=IncidentType.INCIDENTS,
        attributes=IncidentImportRequestAttributes(
            title="Example-Incident",
            visibility=IncidentImportVisibility.ORGANIZATION,
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["import_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.import_incident(body=body)

    print(response)
