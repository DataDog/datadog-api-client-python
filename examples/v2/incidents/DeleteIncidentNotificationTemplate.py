"""
Delete incident notification template returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "notification_template" in the system
NOTIFICATION_TEMPLATE_DATA_ID = environ["NOTIFICATION_TEMPLATE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_notification_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_notification_template(
        id=NOTIFICATION_TEMPLATE_DATA_ID,
    )
