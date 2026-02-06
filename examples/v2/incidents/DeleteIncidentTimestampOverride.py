"""
Delete a timestamp override for an incident returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_incident_timestamp_override"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_timestamp_override(
        incident_id=UUID("9cecfde8-e35d-4387-8985-9b30dcb9cb1c"),
        timestamp_override_id=UUID("6f48a86f-9a39-4bcf-a76b-9a1b20188995"),
    )
