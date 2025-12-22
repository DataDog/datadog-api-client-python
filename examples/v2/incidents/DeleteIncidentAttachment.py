"""
Delete incident attachment returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["delete_incident_attachment"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_attachment(
        incident_id="incident_id",
        attachment_id="00000000-0000-0000-0000-000000000002",
    )
