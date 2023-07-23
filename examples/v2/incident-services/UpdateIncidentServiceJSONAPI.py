"""
Update an existing incident service returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi
from datadog_api_client.v2.model.incident_service_update_request import IncidentServiceUpdateRequestJSON

# there is a valid "service" in the system
SERVICE_DATA_ATTRIBUTES_NAME = environ["SERVICE_DATA_ATTRIBUTES_NAME"]
SERVICE_DATA_ID = environ["SERVICE_DATA_ID"]

body = IncidentServiceUpdateRequestJSON(
    name="service name-updated",
)

configuration = Configuration()
configuration.unstable_operations["update_incident_service"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentServicesApi(api_client)
    response = api_instance.update_incident_service(service_id=SERVICE_DATA_ID, body=body)

    print(response)
