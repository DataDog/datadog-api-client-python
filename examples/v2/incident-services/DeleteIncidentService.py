"""
Delete an existing incident service returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi

# there is a valid "service" in the system
SERVICE_DATA_ID = environ["SERVICE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_service"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentServicesApi(api_client)
    api_instance.delete_incident_service(
        service_id=SERVICE_DATA_ID,
    )
