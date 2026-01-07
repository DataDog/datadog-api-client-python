"""
Delete incident attachment returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# there is a valid "incident_attachment" in the system
INCIDENT_ATTACHMENT_DATA_ID = environ["INCIDENT_ATTACHMENT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_attachment"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_attachment(
        incident_id=INCIDENT_DATA_ID,
        attachment_id=INCIDENT_ATTACHMENT_DATA_ID,
    )
