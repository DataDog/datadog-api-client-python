"""
Get a list of all incident services returns "OK" response
"""

from os import environ
from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi

# there is a valid "service" in the system
SERVICE_DATA_ATTRIBUTES_NAME = environ["SERVICE_DATA_ATTRIBUTES_NAME"]

with ApiClient(Configuration()) as api_client:
    api_instance = IncidentServicesApi(api_client)
    response = api_instance.list_incident_services(filter=SERVICE_DATA_ATTRIBUTES_NAME)

    print(response)
