"""
List timestamp overrides for an incident returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["list_incident_timestamp_overrides"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incident_timestamp_overrides(
        incident_id=UUID("9cecfde8-e35d-4387-8985-9b30dcb9cb1c"),
    )

    print(response)
