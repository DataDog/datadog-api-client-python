"""
Delete an incident notification rule returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_incident_notification_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_notification_rule(
        id=UUID("00000000-0000-0000-0000-000000000001"),
    )
