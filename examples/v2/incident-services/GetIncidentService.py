"""
Get details of an incident service returns "OK" response
"""

from os import environ
from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi

# there is a valid "service" in the system
SERVICE_DATA_ID = environ["SERVICE_DATA_ID"]

with ApiClient(Configuration()) as api_client:
    api_instance = IncidentServicesApi(api_client)
    response = api_instance.get_incident_service(service_id=SERVICE_DATA_ID)

    print(response)
