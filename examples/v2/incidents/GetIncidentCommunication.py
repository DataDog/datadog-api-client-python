"""
Get an incident communication returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_incident_communication"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_communication(
        incident_id="incident_id",
        communication_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
