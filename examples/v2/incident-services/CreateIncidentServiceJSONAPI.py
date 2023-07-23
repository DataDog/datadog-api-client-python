"""
Create a new incident service returns "CREATED" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi
from datadog_api_client.v2.model.incident_service_create_request import IncidentServiceCreateRequestJSON

body = IncidentServiceCreateRequestJSON(
    name="Example-Incident-Service",
)

configuration = Configuration()
configuration.unstable_operations["create_incident_service"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentServicesApi(api_client)
    response = api_instance.create_incident_service(body=body)

    print(response)
